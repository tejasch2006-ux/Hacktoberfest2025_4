import qrcode

data = input("Enter text or link: ")
img = qrcode.make(data)
img.save("qrcode.png")
print("QR Code saved as qrcode.png")
