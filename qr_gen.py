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
  ooo        ooooo ooooooooo.        ooooooooo.         .o.       ooooo      ooo oooooo   oooooo     oooo       .o.       ooooooooo.        
`88.       .888' `888   `Y88.      `888   `Y88.      .888.      `888b.     `8'  `888.    `888.     .8'       .888.      `888   `Y88.      
 888b     d'888   888   .d88'       888   .d88'     .8"888.      8 `88b.    8    `888.   .8888.   .8'       .8"888.      888   .d88'      
 8 Y88. .P  888   888ooo88P'        888ooo88P'     .8' `888.     8   `88b.  8     `888  .8'`888. .8'       .8' `888.     888ooo88P'       
 8  `888'   888   888`88b.          888           .88ooo8888.    8     `88b.8      `888.8'  `888.8'       .88ooo8888.    888`88b.         
 8    Y     888   888  `88b.        888          .8'     `888.   8       `888       `888'    `888'       .8'     `888.   888  `88b.       
o8o        o888o o888o  o888o      o888o        o88o     o8888o o8o        `8        `8'      `8'       o88o     o8888o o888o  o888o                                                                                                                                            
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
