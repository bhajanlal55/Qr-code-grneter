import qrcode
import os
from datetime import datetime

def main():
    print("=== QR Code Generator ===\n")
    
    # User input
    data = input("Aap kis cheez ka QR banana chahte ho? (Link ya text dalen): ")

    # Folder jahan save karna h (Desktop)
    save_folder = os.path.join(os.path.expanduser("~"), "Desktop", "QR_Codes")
    os.makedirs(save_folder, exist_ok=True)

    # Unique file name generate karo
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = os.path.join(save_folder, f"qr_{timestamp}.png")

    # QR code generate karo
    qr = qrcode.QRCode(
        version=1,
        box_size=2,  # chota size ASCII preview ke liye
        border=1
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Image save karo
    img = qr.make_image(fill='black', back_color='white')
    img.save(file_path)

    print(f"\n✅ QR Code generate ho gaya! File: {file_path}")

    # Terminal me ASCII preview
    print("\nQR Code Preview:\n")
    qr.print_ascii(invert=True)

if __name__ == "__main__":
    main()
