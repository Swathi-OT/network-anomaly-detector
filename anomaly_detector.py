from scapy.all import sniff, IP
from collections import Counter
import time

INTERFACE = "eth0"
THRESHOLD = 50
WINDOW = 10

print("=" * 45)
print("       NETWORK ANOMALY DETECTOR")
print("=" * 45)
print(f"Interface : {INTERFACE}")
print(f"Threshold : {THRESHOLD} packets")
print(f"Window    : {WINDOW} seconds")
print("Monitoring started...")
print("Press Ctrl+C to stop")
print()

try:
    while True:
        print(f"\nMonitoring next {WINDOW} seconds...")

        packets = sniff(
            iface=INTERFACE,
            timeout=WINDOW,
            store=True
        )

        source_counts = Counter()

        for packet in packets:
            if IP in packet:
                source_ip = packet[IP].src
                source_counts[source_ip] += 1

        print("\n--- Traffic Summary ---")

        for source_ip, count in source_counts.items():
            print(f"{source_ip} -> {count} packets")

            if count >= THRESHOLD:
                print()
                print("!!! ANOMALY DETECTED !!!")
                print(f"Source IP : {source_ip}")
                print(f"Packets   : {count}")
                print(f"Threshold : {THRESHOLD}")
                print("Reason    : High packet rate")
                print()

except KeyboardInterrupt:
    print("\nDetector stopped.")
