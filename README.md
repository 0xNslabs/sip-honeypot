# Simple SIP Honeypot Server

## Introduction
The Simple SIP Honeypot Server is an easy-to-use script created for cybersecurity practitioners and enthusiasts. Using Python and the Twisted framework, this script sets up a low-interaction Session Initiation Protocol (SIP) server to log SIP requests, acting as a vital tool for basic VoIP traffic analysis and early detection of potential threats in SIP-based communication systems.

## Features
- **Low-Interaction Honeypot**: Designed to mimic SIP services and capture SIP request details with minimal risk.
- **Customizable Server Settings**: Command-line arguments allow for easy configuration of host and port settings.
- **Detailed Logging**: Each SIP request is logged, providing insights for security analysis.
- **Real-time Interaction**: Responds to SIP requests, simulating a live SIP server environment.
- **Educational Tool**: An excellent resource for learning about SIP vulnerabilities and SIP-based attacks.

## Requirements
- Python 3.x
- Twisted Python library

## Installation
To install and run the SIP honeypot server, follow these steps:

```bash
git clone https://github.com/0xNslabs/sip-honeypot.git
cd sip-honeypot
pip install twisted
```

## Usage

Execute the script with optional arguments for host and port. Defaults to 0.0.0.0 (all interfaces) and port 5060.


```bash
python3 sip.py --host 0.0.0.0 --port 5060
```

## Logging

All SIP interactions are logged in sip_honeypot.log for further analysis and research.

## Simple SIP Honeypot In Action

![Simple SIP Honeypot in Action](https://raw.githubusercontent.com/0xNslabs/sip-honeypot/main/PoC.png)
*The image above captures the Simple SIP Honeypot logging real-time SIP queries*

## Security and Compliance
- **Caution**: This server is a honeypot. Employ responsibly in controlled network environments.
- **Compliance**: Adhere to local laws and regulations in deployment.

## License
This project is distributed under the MIT License. See `LICENSE` for more information.