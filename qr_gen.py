import qrcode
import os

# Tool ka naam aur tera naam
tool_name = "HACKING-TOOL v2.2 by Misha Korzhik"
your_name = "Created by [Your Name]"

# User se input lena
data = input("? QR Code me kya dalna chahte ho? URL/Text likho: ")

# QR Code generate karna
img = qrcode.make(data)

# File save karna
img.save("/sdcard/myqrcode.png")

# Output mein tool ka naam, tera naam, aur YouTube link
print(f"\n{tool_name}")
print(f"{your_name}")
print("Tutorial: https://www.youtube.com/watch?v=example")
print("? QR Code ban gaya: /sdcard/myqrcode.png")

# YouTube link ko open karne ka attempt (Termux mein kaam karega agar Android hai)
os.system("am start https://www.youtube.com/watch?v=example")
