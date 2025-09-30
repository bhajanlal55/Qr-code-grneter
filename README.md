# QR Code Generator (Termux)

## Setup

```bash
# ✅ QR Code Generator Setup (Copy-Paste Ready)

# 1. System update & required packages
sudo apt update && sudo apt install python3 python3-venv git -y

# 2. Git repo clone
git clone https://github.com/bhajanlal55/Qr-code-grneter
cd Qr-code-grneter

# 3. Virtual environment create & activate
python3 -m venv qrvenv
source qrvenv/bin/activate

# 4. Required Python package install
pip install qrcode[pil]

ls

python qr_gen.py   

deactivate
