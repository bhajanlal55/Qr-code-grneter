
import qrcode

# User se input lena
data = input("👉 QR Code me kya dalna chahte ho? URL/Text likho: ")

# QR Code generate karna
img = qrcode.make(data)

# File save karna
img.save("/sdcard/myqrcode.png")

print("✅ QR Code ban gaya: /sdcard/myqrcode.png")
