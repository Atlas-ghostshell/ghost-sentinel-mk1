# ghost-sentinel-mk1
SSH Brute-force Detection &amp; Auto-Mitigation using iptables + systemd

# Ghost-Sentinel Mk1

**SSH Brute-force Detection & Auto-Mitigation Tool**

Ghost-Sentinel Mk1 is a Python-based defensive security tool designed to monitor real-time SSH authentication logs and automatically mitigate brute-force attacks. Offending IPs are banned for a set duration using `iptables`, and the script is configured to run persistently with `systemd`.

---

## Features

- Real-time SSH brute-force detection using `journalctl`
- Auto-bans offending IPs after 3 failed attempts
- One-hour automatic unban
- Persistent via systemd
- Lightweight and fast for on-prem or VM use

---

## Setup

1. **Install** the script:
   ```bash
   sudo mkdir -p /opt/ghost-sentinel
   sudo cp ghost_sentinel_mk1.py /opt/ghost-sentinel/

Create systemd service(optional):  /etc/systemd/system/ghost-sentinel.service:

[Unit]
Description=Ghost-Sentinel Mk1 - SSH Brute-force Defense
After=network.target

[Service]
ExecStart=/usr/bin/python3 /opt/ghost-sentinel/ghost_sentinel_mk1.py
Restart=always

[Install]
WantedBy=multi-user.target

Reload and start service:

    sudo systemctl daemon-reload
    sudo systemctl enable ghost-sentinel.service
    sudo systemctl start ghost-sentinel.service

Sample Output

[*] Ghost-Sentinel Mk1 activated. Watching for SSH brute-force attempts...
[!] 3 failed attempts detected from 192.168.1.100 - BANNED for 1 hour

Author

Geoffrey Muriuki Mwangi
Cybersecurity Student | Purple Teamer | Builder of digital fortresses
Email: muriukigeoffrey472@gmail.com
LinkedIn: https://www.linkedin.com/in/geoffrey-muriuki-b4ba71306
In Collaboration With:

Atlas (ChatGPT)
Your loyal AI cybersecurity partner — powering automation, analysis, and defense
Built by OpenAI to assist in building ethical, resilient systems
