from tkinter import *   #tkinter package
from tkinter import ttk
# Api cal module:
import requests

# weather Api
def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=EnterApiId").json()
    # pass data into trhe labels:
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15))+" °C")
    pr_label1.config(text=data["main"]["pressure"])

win = Tk() #tkinter class
win.title("Today Weather")
win.config(bg="darkkhaki") #background-color
win.geometry("500x550") #size of the frame

#label of the boxe[Heading]:
name_label = Label(win,text="Today Weather",font=("Time new Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)
name_label.config(bg="khaki")

# combo box:
city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="Weather",values=list_name,font=("Time New Roman",15,"bold"),textvariable=city_name)

# name_label.place(x=25,y=50,height=50,width=450)
com.place(x=25, y=120, height=50, width=450)

# output data:
w_label = Label(win,text="Weather Climate",font=("Time new Roman",10,"bold"))
w_label.place(x=25,y=260,height=50,width=210)

w_label1 = Label(win,text="",font=("Time new Roman",10,"bold"))
w_label1.place(x=250,y=260,height=50,width=224)

wb_label = Label(win,text="Weather Description",font=("Time new Roman",10,"bold"))
wb_label.place(x=25,y=330,height=50,width=210)

wb_label1 = Label(win,text=" ",font=("Time new Roman",10,"bold"))
wb_label1.place(x=250,y=330,height=50,width=224)

temp_label = Label(win,text="Temprature",font=("Time new Roman",10,"bold"))
temp_label.place(x=25,y=400,height=50,width=210)

temp_label1 = Label(win,text="",font=("Time new Roman",10,"bold"))
temp_label1.place(x=250,y=400,height=50,width=224)

pr_label = Label(win,text="Pressure",font=("Time new Roman",10,"bold"))
pr_label.place(x=25,y=470,height=50,width=210)

pr_label1 = Label(win,text="",font=("Time new Roman",10,"bold"))
pr_label1.place(x=250,y=470,height=50,width=224)

# button
done_button = Button(win,text="Check",font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)

win.mainloop() #Gui call