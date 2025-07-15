import qrcode 

data = input("Enter the text or URL: ").strip().lower()
filename = input("Enter the filename:").strip().lower()
qr = qrcode.QRCode(box_size=10,border=4)
qr.add_data(data)
image = qr.make_image(fill_color="black",back_color="white")
image.save(filename)
print(f"QrCode saved as {filename}")

