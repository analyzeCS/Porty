import socket
import os
import time
import sys


os.system("cls" if os.name == "nt" else "clear")


banner = """

:::::::::   ::::::::  ::::::::: ::::::::::: :::   ::: 
:+:    :+: :+:    :+: :+:    :+:    :+:     :+:   :+: 
+:+    +:+ +:+    +:+ +:+    +:+    +:+      +:+ +:+  
+#++:++#+  +#+    +:+ +#++:++#:     +#+       +#++:   
+#+        +#+    +#+ +#+    +#+    +#+        +#+    
#+#        #+#    #+# #+#    #+#    #+#        #+#    
###         ########  ###    ###    ###        ###    

"""

print(banner)
center = "Made by Attack"
middle = center.center(50)
print(middle)

center2 = "t.me/mumbus200"
middle2 = center2.center(50)
print(middle2)

center3 = "github.com/analyzeCS"
middle3 = center3.center(50)
print(middle3)

print("\n")
print("=" * 50)

user_ip = input("Enter the IP adress you want to scan: ")

if user_ip != int and user_ip != "localhost":
    print("You must enter an IP address to scan.")
    sys.exit(1)


ports = list(range(1, 1025))

slider = "-\\|/"
for _ in range(10):
    for char in slider:
        sys.stdout.write((f"\r{char} Scanning ports... "))
        sys.stdout.flush()
        time.sleep(0.1)
print("\n")


def scan_port(ip, port,):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        s.connect((ip, port))
        s.close()
        return True
    except:
        s.close()
        return False


for port in ports:
    if scan_port(user_ip, port):
        print(f"Port {port} is open")


print("\nScan complete.")
time.sleep(2)
