# Home-Network-IDS

# Languages & Programs Used:
Python
Visual Studio Code
Pushover API Key & App
Winotify

# Purpose:
The Network Connection Monitor is a robust tool designed to monitor network connections and provide real-time notifications when a new device connects to the network. This project showcases practical skills in Python, network packet analysis with Scapy, Windows notification using winotify, and push notification integration using the Pushover API. It serves as a valuable asset for network administrators and cybersecurity enthusiasts seeking to enhance network visibility and security.

# Key Features:
Network Packet Analysis: The tool utilizes Scapy, a powerful packet manipulation library, to analyze network packets and extract information about new device connections.

JSON Log File: The tool maintains a JSON log file to keep track of known devices that have previously connected to the network.

Windows Notification: The winotify library enables the tool to send Windows notifications when a new device connects, providing real-time alerts to administrators.

Push Notification Integration: The tool integrates with the Pushover API, allowing it to send push notifications to mobile devices, ensuring administrators stay informed even when away from their workstations.

User-Friendly Interface: The script is designed to be executed via the command line, providing administrators with a straightforward and efficient means of monitoring network connections.

# Skills Gained:
Packet Analysis with Scapy: The project showcases expertise in using Scapy to capture, dissect, and interpret network packets, facilitating network monitoring and analysis.

File I/O and JSON Handling: The tool effectively loads and saves known devices' information in a JSON log file, ensuring persistent and reliable data storage.

Windows Notification: Leveraging the winotify library, the project demonstrates the ability to send Windows notifications, promoting a seamless user experience.

API Integration: The integration with the Pushover API illustrates the ability to interact with external services and deliver push notifications to mobile devices.

Network Monitoring and Security: The project highlights practical knowledge of network monitoring techniques and their relevance in cybersecurity.

# Usage:
Ensure that the required libraries (scapy, winotify, requests) are installed.

Set the LOG_FILE variable to the desired path for the JSON log file.

Set the PUSHOVER_API_TOKEN and PUSHOVER_USER_KEY variables with your Pushover API token and user key.

Run the script to start monitoring network connections.

When a new device connects to the network, the tool will send both a Windows notification and a push notification to the specified device.

# Contributions
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, feel free to create a pull request or submit an issue on GitHub.

# License
This project is licensed under the MIT License.
