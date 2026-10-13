# Network Anomaly Detector Using Scapy

## About the Project

This is a beginner-friendly Python-based network monitoring
project that uses Scapy to capture network packets and identify
potentially unusual traffic patterns.

## Features

- Captures network packets using Scapy.
- Counts packets from each source IP address.
- Displays a traffic summary.
- Generates an alert when a source IP reaches the configured
  packet-count threshold.
- Allows monitoring to be stopped using Ctrl+C.

## Technologies Used

- Python
- Scapy
- Kali Linux
- Networking fundamentals

## Configuration

- Network interface: eth0
- Packet threshold: 50
- Monitoring window: 10 seconds

These values can be modified in the Python script.

## How to Run

Install Scapy:

    python3 -m pip install scapy

Run the detector with the required permissions:

    sudo python3 anomaly_detector.py

Check the network interface name before running the program.

## Learning Objectives

- Understand packet capture.
- Learn source IP address analysis.
- Monitor network traffic.
- Understand basic network anomaly detection.

## Disclaimer

This project is intended for educational use and authorized
network monitoring only.
