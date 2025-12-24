# QR Code Generator using Python

import qrcode 
url =input("Enter URL: ")
img = qrcode.make(url)
img.save("qrcode.png")
print("QR code generated and saved as qrcode.png")