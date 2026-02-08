# Porty

## Description
Porty is a fast and efficient port scanner designed to help network administrators and security professionals identify open ports and services running on networked devices.

## Features
- Fast scanning using asynchronous techniques.
- Scan multiple IP addresses simultaneously.
- Customizable scan options including port ranges and protocols.
- Detailed output formats (text, JSON).

## Installation
```bash
# Install dependencies
pip install -r requirements.txt
```

## Usage
```bash
# Basic usage
python porty.py -t <target_ip>
```

## Requirements
- Python 3.6+
- Scapy library
- Asyncio library

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.