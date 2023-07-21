import json
from scapy.all import *
from winotify import Notification
import requests

LOG_FILE = "known_devices.json"  # Path to the JSON log file

PUSHOVER_API_TOKEN = "ap6joxaidky2ttoy44dmfbahatmian"
PUSHOVER_USER_KEY = "ut2wwp9ae1k3o43evzqpjzmdca6kkt"

def load_known_devices():
    """
    Load known devices from the JSON log file.
    """
    try:
        with open(LOG_FILE, "r") as file:
            known_devices = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        known_devices = []
    
    return known_devices

def save_known_devices(known_devices):
    """
    Save known devices to the JSON log file.
    """
    with open(LOG_FILE, "w") as file:
        json.dump(known_devices, file, indent=4)

def send_notification(title, message):
    """
    Send a Windows notification using winotify.
    """
    notification = Notification(title, message)
    notification.show()

def send_push_notification(title, message):
    """
    Send a push notification using Pushover.
    """
    url = "https://api.pushover.net/1/messages.json"
    data = {
        "token": "ap6joxaidky2ttoy44dmfbahatmian",
        "user": "ut2wwp9ae1k3o43evzqpjzmdca6kkt",
        "title": title,
        "message": message
    }
    requests.post(url, data=data)


def detect_network_connections():
    """
    Monitor network connections and send notifications when a new device connects.
    """
    known_devices = load_known_devices()

    def handle_packet(packet):
        if packet.haslayer(DHCP) and packet.haslayer(IP):
            mac_address = packet[Ether].src
            ip_address = packet[IP].src
            if mac_address not in known_devices:
                print(f"New device connected! MAC address: {mac_address}, IP address: {ip_address}")
                # Send a notification when a new device connects
                send_notification("New Device Connected", f"MAC address: {mac_address}, IP address: {ip_address}")
                send_push_notification("New Device Connected", f"MAC address: {mac_address}, IP address: {ip_address}")

                known_devices.append({
                    "mac_address": mac_address,
                    "ip_address": ip_address
                })  # Add the new device to the known devices list

                save_known_devices(known_devices)  # Save the updated known devices to the log file

    # Start sniffing network packets
    sniff(prn=handle_packet, filter="udp and (port 67 or 68)", store=0)

# Run the network connection detection
detect_network_connections()