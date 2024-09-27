import qrcode

# Collect user information
name = input("Enter your name: ")
address = input("Enter your address: ")
contact = input("Enter your contact number: ")
profession = input("Enter your profession: ")

# Create the data string for QR code
data = f"Name: {name}\nAddress: {address}\nContact: {contact}\nProfession: {profession}"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to QR code
qr.add_data(data)
qr.make(fit=True)

# Create the QR code image
img = qr.make_image(fill="black", back_color="white")

# Save the QR code as an image file
img.save("user_info_qrcode.png")

print("QR Code generated and saved as 'user_info_qrcode.png'")
