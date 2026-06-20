from scapy.all import sniff, IP, TCP
from collections import defaultdict
from datetime import datetime

# Track connection attempts
connection_count = defaultdict(int)

# Threshold for alerts
PORT_SCAN_THRESHOLD = 20

def log_alert(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[ALERT] {timestamp} - {message}")

def analyze_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        # Detect TCP traffic
        if TCP in packet:
            dst_port = packet[TCP].dport

            # Count connections per source IP
            connection_count[src_ip] += 1

            # Basic port scan detection
            if connection_count[src_ip] > PORT_SCAN_THRESHOLD:
                log_alert(
                    f"Possible Port Scan Detected from {src_ip}"
                )

            print(
                f"TCP Packet | Source: {src_ip} "
                f"| Destination: {dst_ip} "
                f"| Port: {dst_port}"
            )

def start_ids():
    print("=" * 50)
    print("Simple Network Intrusion Detection System")
    print("Monitoring network traffic...")
    print("=" * 50)

    sniff(
        prn=analyze_packet,
        store=False
    )

if __name__ == "__main__":
    start_ids()
