# pip install pikepdf
import pikepdf

old_pdf = pikepdf.pdf.open("pdf_name.pdf")

no_ext = pikepdf.Permissions(extract = False)

old_pdf.save("pro_new.pdf",encryption=pikepdf.Encryption(user = "123",owner="san",allow=no_ext))
