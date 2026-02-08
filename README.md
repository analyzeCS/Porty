# Port Scanner

This is a simple port scanner written in Python, named `port_scanner.py`. It scans the ports from 1 to 1024 on a specified IP address while establishing socket connections with a timeout of 0.5 seconds. 

## Features
- Scans ports 1-1024
- 0.5 second timeout for socket connections
- Displays a cool ASCII banner
- Takes user input for target IP address

## Usage
Simply run the script and provide the target IP address when prompted. The scanner will check the specified ports and report if they are open or closed.

## Example
```bash
python port_scanner.py
```

Follow the prompts to scan the desired IP address!