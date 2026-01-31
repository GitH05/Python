import tkinter as tk
from tkinter import messagebox, ttk
import pymysql
from datetime import date
import math

# --- Database configuration ---
DB_CONFIG = {
    'host': 'localhost',
    'user': 'ENTER-YOUR-MYSQL-DATABASE-USER-NAME(root)',
    'password': 'ENTER-YOUR-MAYSQL-DATABASE-PASSWORD', 
    'database': 'ENTER-YOUR-DATABASE-NAME',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

class CollegeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("College Management Professional")
        self.root.geometry("700x850")
        self.root.configure(bg="#f8f9fa")
        
        # Data variables
        self.current_page = 0
        self.rows_per_page = 8 
        self.total_students = []
        self.filtered_students = [] 

        # --- SCROLLBAR SYSTEM ---
        self.main_container = tk.Frame(self.root)
        self.main_container.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.main_container, bg="#f8f9fa", highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(self.main_container, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#f8f9fa")
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(self.canvas_frame, width=e.width))
        self.canvas.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

        self.setup_ui()
        self.refresh_data() # Load data immediately

    def get_db_connection(self):
        try:
            return pymysql.connect(**DB_CONFIG)
        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", f"Failed to connect to DB:\n{e}")
            return None

    def setup_ui(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=('Helvetica', 10, 'bold'), background="#ecf0f1")
        style.configure("Treeview", rowheight=30, font=('Segoe UI', 9))
        
        # --- Header ---
        header = tk.Label(self.scrollable_frame, text="ATTENDANCE ADMINISTRATION SYSTEM", font=("Helvetica", 18, "bold"), 
                          bg="#2c3e50", fg="white", pady=15)
        header.pack(fill="x")

        # --- Student Entry ---
        f_entry = tk.LabelFrame(self.scrollable_frame, text=" Student Registration ", font=("Arial", 10, "bold"), bg="#f8f9fa", padx=20, pady=10)
        f_entry.pack(fill="x", padx=30, pady=10)

        fields = [("Name *", "name"), ("Email *", "email"), ("Dept", "dept"), ("Class", "class")]
        self.entries = {}
        for i, (label, key) in enumerate(fields):
            tk.Label(f_entry, text=label, bg="#f8f9fa", font=("Arial", 9)).grid(row=i//2, column=(i%2)*2, sticky="w", pady=2)
            ent = tk.Entry(f_entry, width=25, relief="solid", borderwidth=1)
            ent.grid(row=i//2, column=(i%2)*2+1, padx=10, pady=2)
            self.entries[key] = ent

        tk.Button(f_entry, text="Add Student", command=self.add_student, bg="#27ae60", fg="white", 
                  width=15, relief="flat", font=("Arial", 9, "bold")).grid(row=2, column=0, columnspan=4, pady=10)

        # --- Attendance ---
        f_att = tk.LabelFrame(self.scrollable_frame, text=" Attendance Logging ", font=("Arial", 10, "bold"), bg="#f8f9fa", padx=20, pady=10)
        f_att.pack(fill="x", padx=30, pady=5)

        self.dropdown = ttk.Combobox(f_att, width=40, state="readonly")
        self.dropdown.grid(row=0, column=1, pady=5, padx=10)
        self.status_cb = ttk.Combobox(f_att, values=['Present', 'Absent', 'Late', 'Excused'], state="readonly", width=40)
        self.status_cb.current(0)
        self.status_cb.grid(row=1, column=1, pady=5, padx=10)

        tk.Button(f_att, text="Submit Attendance", command=self.submit_attendance, bg="#2980b9", fg="white", 
                  width=20, relief="flat", font=("Arial", 9, "bold")).grid(row=2, column=0, columnspan=2, pady=5)

        # --- SEARCH SECTION ---
        f_search = tk.Frame(self.scrollable_frame, bg="#f8f9fa")
        f_search.pack(fill="x", padx=30, pady=(15, 0))
        
        # Label for the search bar
        tk.Label(f_search, text="🔍 Search:", font=("Arial", 10, "bold"), bg="#f8f9fa").pack(side="left")
        
        self.search_var = tk.StringVar()
        self.search_var.trace("w", lambda name, index, mode: self.apply_filter())
        
        self.search_ent = tk.Entry(f_search, textvariable=self.search_var, font=("Arial", 10), 
                                   width=25, relief="solid", borderwidth=1)
        self.search_ent.pack(side="left", padx=10)

        # --- DASHBOARD TABLE ---
        f_table = tk.LabelFrame(self.scrollable_frame, text=" Live Dashboard ", font=("Arial", 10, "bold"), bg="white", padx=10, pady=10)
        f_table.pack(fill="x", padx=30, pady=5)

        cols = ("ID", "Name", "Department", "Attendance %")
        self.tree = ttk.Treeview(f_table, columns=cols, show='headings', height=self.rows_per_page) 
        for col in cols:
            self.tree.heading(col, text=col, anchor="center")
            self.tree.column(col, anchor="center", width=120)

        scroll = ttk.Scrollbar(f_table, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        # --- Pagination ---
        f_page = tk.Frame(self.scrollable_frame, bg="#f8f9fa")
        f_page.pack(pady=5)
        self.btn_prev = tk.Button(f_page, text="← Prev", command=self.prev_page)
        self.btn_prev.pack(side="left", padx=5)
        self.page_label = tk.Label(f_page, text="Page 1", bg="#f8f9fa", font=("Arial", 9, "bold"))
        self.page_label.pack(side="left", padx=5)
        self.btn_next = tk.Button(f_page, text="Next →", command=self.next_page)
        self.btn_next.pack(side="left", padx=5)

        # --- Actions ---
        f_btns = tk.Frame(self.scrollable_frame, bg="#f8f9fa")
        f_btns.pack(pady=10)
        tk.Button(f_btns, text="📊 View Report", command=self.view_attendance_report, bg="lightblue", width=20).grid(row=0, column=0, padx=5)
        tk.Button(f_btns, text="⚠️ Alerts", command=self.check_alerts, bg="#e67e22", fg="white", width=20).grid(row=0, column=1, padx=5)

    def refresh_data(self):
        conn = self.get_db_connection()
        if not conn: return
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT student_id, name FROM students ORDER BY name")
                rows = cursor.fetchall()
                self.dropdown['values'] = [f"{r['student_id']}: {r['name']}" for r in rows]
                
                cursor.execute("""
                    SELECT s.student_id, s.name, s.department,
                           SUM(CASE WHEN a.status='Present' THEN 1 ELSE 0 END) AS present,
                           COUNT(a.attendance_id) AS total
                    FROM students s
                    LEFT JOIN attendance_records a ON s.student_id = a.student_id
                    GROUP BY s.student_id ORDER BY s.created_date DESC
                """)
                self.total_students = cursor.fetchall()
                self.apply_filter() # Initialize view with search filter (even if empty)
        finally:
            conn.close()

    def apply_filter(self):
        query = self.search_var.get().lower()
        self.filtered_students = []
        
        for s in self.total_students:
            perc = f"{(s['present'] / s['total'] * 100):.1f}%" if s['total'] > 0 else "0.0%"
            # Search logic 
            match = (query in str(s['student_id']).lower() or 
                     query in s['name'].lower() or 
                     query in (s['department'] or "").lower() or 
                     query in perc)
            if match:
                self.filtered_students.append(s)
        
        self.current_page = 0
        self.update_table_view()

    def update_table_view(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        start = self.current_page * self.rows_per_page
        end = start + self.rows_per_page
        page_data = self.filtered_students[start:end]

        for row in page_data:
            perc = (row['present'] / row['total'] * 100) if row['total'] > 0 else 0
            self.tree.insert("", tk.END, values=(row['student_id'], row['name'], row['department'], f"{perc:.1f}%"))

        total_pages = max(1, math.ceil(len(self.filtered_students)/self.rows_per_page))
        self.page_label.config(text=f"Page {self.current_page + 1} of {total_pages}")
        self.btn_prev.config(state="normal" if self.current_page > 0 else "disabled")
        self.btn_next.config(state="normal" if end < len(self.filtered_students) else "disabled")

    def next_page(self):
        self.current_page += 1
        self.update_table_view()

    def prev_page(self):
        self.current_page -= 1
        self.update_table_view()

    def add_student(self):
        data = (self.entries['name'].get(), self.entries['email'].get(), self.entries['dept'].get(), self.entries['class'].get())
        if not data[0] or not data[1]:
            messagebox.showwarning("Warning", "Name and Email are required!")
            return
        conn = self.get_db_connection()
        if conn:
            try:
                with conn.cursor() as cursor:
                    cursor.execute("INSERT INTO students (name, email, department, class) VALUES (%s, %s, %s, %s)", data)
                    conn.commit()
                for e in self.entries.values(): e.delete(0, tk.END)
                self.refresh_data()
            finally: conn.close()

    def submit_attendance(self):
        if not self.dropdown.get():
            messagebox.showwarning("Warning", "Select a student first!")
            return
        sid = self.dropdown.get().split(":")[0]
        conn = self.get_db_connection()
        if conn:
            try:
                with conn.cursor() as cursor:
                    cursor.execute("INSERT INTO attendance_records (student_id, attendance_date, status) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE status=VALUES(status)",
                                   (sid, date.today(), self.status_cb.get()))
                    conn.commit()
                self.refresh_data()
            finally: conn.close()

    def view_attendance_report(self):
        report_window = tk.Toplevel(self.root)
        report_window.title("Detailed Report")
        report_window.geometry("600x400")
        tree = ttk.Treeview(report_window, columns=("ID", "Full Name", "Present", "Total", "Attendace(%)"), show='headings')
        for col in ("ID", "Full Name", "Present", "Total", "Attendace(%)"):
            tree.heading(col, text=col, anchor="center")
            tree.column(col, anchor="center", width=100)
        tree.pack(fill="both", expand=True, padx=10, pady=10)
        for row in self.total_students:
            perc = (row['present'] / row['total'] * 100) if row['total'] > 0 else 0
            tree.insert("", tk.END, values=(row['student_id'], row['name'], row['present'], row['total'], f"{perc:.1f}%"))

    def check_alerts(self):
        conn = self.get_db_connection()
        if not conn: return
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT percentage_limit FROM attendance_thresholds ORDER BY id DESC LIMIT 1")
                res = cursor.fetchone()
                limit = float(res['percentage_limit']) if res else 75.0
                alerts = [f"{st['name']} ({ (st['present']/st['total']*100):.1f}%)" for st in self.total_students if st['total'] > 0 and (st['present']/st['total']*100) < limit]
                if alerts: messagebox.showwarning("Low Attendance", f"Students below {limit}%:\n\n" + "\n".join(alerts))
                else: messagebox.showinfo("Safe", f"No students below {limit}% threshold.")
        finally: conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = CollegeApp(root)
    root.mainloop()