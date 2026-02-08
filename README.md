# PORTY - Port Scanner
```
:::::::::   ::::::::  ::::::::: ::::::::::: :::   ::: 
:+:    :+: :+:    :+: :+:    :+:    :+:     :+:   :+: 
+:+    +:+ +:+    +:+ +:+    +:+    +:+      +:+ +:+  
+#++:++#+  +#+    +:+ +#++:++#:     +#+       +#++:   
+#+        +#+    +#+ +#+    +#+    +#+        +#+    
#+#        #+#    #+# #+#    #+#    #+#        #+#    
###         ########  ###    ###    ###        ###    
```

A simple, fast port scanner written in Python that scans the first 1024 ports of a target IP address.

## Features

- 🔍 Scans ports 1-1024
- ⚡ Fast scanning speed with socket timeouts
- 🎨 Animated scanning display
- 💻 Cross-platform (Windows, Linux, macOS)
- 🎯 Easy to use

## Requirements

- Python 3.x
- No external libraries required (uses only Python Standard Library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/analyzeCS/portxy.git
cd porty
```

2. Run the script:
```bash
python porty.py
```

## Usage

1. Start the script:
```bash
python porty.py
```

2. Enter the IP address to scan:
```
Enter the IP adress you want to scan: 192.168.1.1
```

3. Wait for the scan results:
```
/ Scanning ports... 

Port 22 is open
Port 80 is open
Port 443 is open

Scan complete.
```

## Examples

**Scan local network:**
```bash
# Example: Scan router
Enter the IP adress you want to scan: 192.168.1.1
```

**Scan localhost:**
```bash
Enter the IP adress you want to scan: localhost
```

**Scan external IP:**
```bash
Enter the IP adress you want to scan: 8.8.8.8
```

## How It Works

The scanner uses TCP socket connections to check if ports are open:
- **Timeout:** 0.5 seconds per port
- **Scan range:** Ports 1-1024 (Well-known ports)
- **Method:** TCP Connect Scan

## Common Open Ports

| Port | Service |
|------|---------|
| 21   | FTP     |
| 22   | SSH     |
| 23   | Telnet  |
| 25   | SMTP    |
| 80   | HTTP    |
| 443  | HTTPS   |
| 3306 | MySQL   |
| 3389 | RDP     |

## Legal Notice

⚠️ **IMPORTANT:** This tool should only be used for legal purposes!

- Only scan systems for which you have explicit permission
- Scanning foreign systems without authorization is illegal in many countries
- Use this tool only for educational purposes or on your own systems
- The author assumes no liability for misuse

## Limitations

- Only scans the first 1024 ports
- No UDP support
- No service detection
- Simple TCP Connect Scan (can be detected by firewalls/IDS)

## Planned Features

- [ ] Extended port range (custom range)
- [ ] Multi-threading for faster scans
- [ ] Service detection
- [ ] Export results (JSON/CSV)
- [ ] UDP port scanning
- [ ] Banner grabbing

## Troubleshooting

**Problem:** "You must enter an IP address to scan."
- **Solution:** Enter a valid IP address or "localhost"

**Problem:** No open ports found
- **Solution:** 
  - Check the IP address
  - Firewall might be blocking scans
  - Target host might be offline

**Problem:** Script hangs while scanning
- **Solution:** Adjust timeout value in `s.settimeout(0.5)`

## License

This project is intended for educational purposes. Please use it responsibly.

---

⭐ If you like this project, give it a star on GitHub!
