import qrcode
import os
import time

# Colors (ANSI escape codes)
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
MAGENTA = "\033[1;35m"
RESET = "\033[0m"

def banner():
    os.system("clear")  # Screen clear karega (Linux/Termux me)
    print(f"""{GREEN}

                  .-"      "-.
                 /            \
                |              |
                |,  .-.  .-.  ,|
                | )(__/  \__)( |
                |/     /\     \|
      (@_       (_     ^^     _)
 _     ) \_______\__|IIIIII|__/__________________________
(_)@8@8{}<________|-\IIIIII/-|___________________________>
       )_/        \          /
      (@           `--------` jgs
 {RESET}""")
    print(f"{BLUE}<========================================================>{RESET}")
    print(f"{YELLOW}          WELCOME TO QR Code Generator{RESET}")
    print(f"{CYAN}              Created by:BHAJANLAL55{RESET}")
    print(f"{BLUE}<========================================================>{RESET}\n")
    time.sleep(100)  # 2 second rukega banner dikhane ke liye

# --- MAIN CODE ---
banner()
data = input(f"{MAGENTA}[+] Enter text/URL for QR Code: {RESET}")
img = qrcode.make(data)
img.save("/sdcard/myqrcode.png")
print(f"{GREEN}[✓] QR Code saved successfully in /sdcard/myqrcode.png {RESET}")
