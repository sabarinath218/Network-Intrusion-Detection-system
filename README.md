# Simple Network Intrusion Detection System (NIDS)

## Overview

This project implements a basic **Network Intrusion Detection System (NIDS)** using Python and Scapy. It monitors network traffic in real time, analyzes TCP packets, and detects potential port scanning activities based on connection patterns.

The system captures packets from the network interface, extracts source and destination information, and generates alerts when suspicious behavior is identified.

## Features

* Real-time packet capture and analysis
* TCP traffic monitoring
* Source and destination IP tracking
* Connection counting per source IP
* Basic port scan detection
* Alert generation for suspicious activity
* Lightweight and easy-to-understand implementation

## Technologies Used

* Python 3
* Scapy
* Collections (defaultdict)
* Datetime

## How It Works

1. Captures network packets using Scapy.
2. Extracts IP and TCP header information.
3. Tracks connection attempts from each source IP.
4. Detects potential port scans when connection attempts exceed a predefined threshold.
5. Generates alerts for suspicious activity.

## Installation

```bash
pip install scapy
```

## Usage

Run the script with administrator/root privileges:

```bash
sudo python ids.py
```

## Sample Output

```text
==================================================
Simple Network Intrusion Detection System
Monitoring network traffic...
==================================================

TCP Packet | Source: 192.168.1.10 | Destination: 192.168.1.1 | Port: 80

[ALERT] 2026-06-20 12:00:00 - Possible Port Scan Detected from 192.168.1.10
```

## Detection Logic

The IDS maintains a count of TCP connection attempts from each source IP address. If the number of connections exceeds the configured threshold (`PORT_SCAN_THRESHOLD`), an alert is generated indicating a possible port scan.

## Future Enhancements

* Detection of SYN flood attacks
* Support for UDP and ICMP monitoring
* Logging alerts to files
* Email or SMS notifications
* Dashboard visualization
* Machine learning–based anomaly detection
