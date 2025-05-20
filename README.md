# ghost-sentinel-mk1
SSH Brute-force Detection &amp; Auto-Mitigation using iptables + systemd


Ghost-Sentinel Mk1 is a real-time SSH brute-force detection and mitigation tool written in Python. It monitors authentication logs using journalctl, detects multiple failed login attempts from the same IP address, and automatically blocks those IPs using iptables. Offending IPs are unbanned after a set period — ensuring dynamic protection without manual intervention.

Features

 Real-time SSH log monitoring

 Detects multiple failed login attempts (default: 3 failures)

 Blocks attackers via iptables

 Auto-unbans IPs after 1 hour

 Runs as a persistent daemon with root privileges

 Lightweight and customizable

How It Works

 Uses journalctl -kf to stream live SSH logs.

 Extracts the rhost field (source IP) from failed authentication entries.

 Tracks failed login attempts per IP address.

 On exceeding the threshold (3), the IP is blocked via iptables.

 Banned IPs are tracked with a timestamp.

 After 1 hour, IPs are automatically unbanned.

Installation

 Clone the repository:

      git clone https://github.com/Atlas-ghostshell/ghost-sentinel.git
      cd ghost-sentinel

Move the script to a secure directory (e.g., /opt/ghost-sentinel/):

sudo mkdir -p /opt/ghost-sentinel
sudo cp ghost_sentinel_mk1.py /opt/ghost-sentinel/

Make it executable:

    sudo chmod +x /opt/ghost-sentinel/ghost_sentinel_mk1.py

Running the Script

Manual run (testing):

      sudo python3 /opt/ghost-sentinel/ghost_sentinel_mk1.py

Persistent setup:

You can run Ghost-Sentinel Mk1 as a background daemon using a systemd service. This ensures it starts automatically on boot and runs with root privileges.

Requirements

    Python 3.x

    Root privileges (for iptables operations)

    System using systemd and journalctl

Disclaimer

This script is for educational purposes and lab environments. Ensure proper security and logging configurations before deploying in production.
License

MIT License

Author

Geoffrey Muriuki Mwangi
Cybersecurity Student | Purple Teamer | Builder of digital fortresses
Email: muriukigeoffrey472@gmail.com
LinkedIn: https://www.linkedin.com/in/geoffrey-muriuki-b4ba71306
In Collaboration With:

Atlas (ChatGPT)
My loyal AI cybersecurity partner — powering automation, analysis, and defense
Built by OpenAI to assist in building ethical, resilient systems
