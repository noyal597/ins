from time import time
from datetime import datetime

suspicious_sources = ["unknown", "192.168.1.100"]
suspicious_ports = [21, 23]
traffic_data = [
        {"source": "192.168.1.1", "dest": "10.0.0.1", "port": 22, "payload": "SSH Connection", "protocol": "TCP"},
        {"source": "10.0.0.2", "dest": "192.168.1.2", "port": 80, "payload": "HTTP request", "protocol": "TCP"},
        {"source": "10.0.0.3", "dest": "10.0.0.1", "port": 21, "payload": "FTP transfer", "protocol": "TCP"},
        {"source": "unknown", "dest": "192.168.1.1", "port": 443, "payload": "sus", "protocol": "TCP"},
        ]

def is_suspicious(packet):
    return packet["source"] in suspicious_sources or \
        packet["port"] in suspicious_ports

def generate_alert(packet):
    msg = "Suspicious packet detected.\n"
    msg += "Time: %s\n" %datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for key, value in packet.items():
        msg += "%s: %s\n" %(key, value)
    return msg

def log_alert(msg):
    with open("alerts.log", "a") as f:
        f.write(msg + '\n')

if __name__ == '__main__':
    for packet in traffic_data:
        if is_suspicious(packet):
            msg = generate_alert(packet)
            print(msg)
            log_alert(msg)
