# Qr-code-grneter
My name is mr . bhajanlal 
pkg install python -y
pip install qrcode
pip install pillow
python <<EOF
import qrcode
img = qrcode.make("https://google.com")
img.save("/sdcard/myqrcode.png")
EOF
