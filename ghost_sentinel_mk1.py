#!/usr/bin/env python3

import subprocess
import re
import time
from collections import defaultdict
from datetime import datetime, timedelta

# CONFIG
BAN_THRESHOLD = 3
BAN_DURATION = timedelta(hours=1)
JOURNALCTL_CMD = ["journalctl", "-f", "-n", "0", "-o", "short", "_COMM=sshd"]

# TRACKER
failure_counts = defaultdict(int)
ban_list = {}

# REGEX to extract failed auth IP
FAILURE_REGEX = re.compile(r"Failed password for .* from ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)")

def ban_ip(ip):
    print(f"[+] Banning IP: {ip}")
    subprocess.run(["iptables", "-I", "INPUT", "-s", ip, "-j", "DROP"])
    ban_list[ip] = datetime.now()

def unban_ip(ip):
    print(f"[+] Unbanning IP: {ip}")
    subprocess.run(["iptables", "-D", "INPUT", "-s", ip, "-j", "DROP"])
    del ban_list[ip]
    failure_counts[ip] = 0

def monitor():
    print("[*] Ghost-Sentinel Mk1 activated. Watching for SSH brute-force attempts...")
    process = subprocess.Popen(JOURNALCTL_CMD, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    while True:
        line = process.stdout.readline()
        if not line:
            continue

        match = FAILURE_REGEX.search(line)
        if match:
            ip = match.group(1)
            failure_counts[ip] += 1
            print(f"[-] Failed login from {ip} ({failure_counts[ip]}x)")

            if failure_counts[ip] == BAN_THRESHOLD:
                ban_ip(ip)

        # Check for expired bans
        for ip in list(ban_list.keys()):
            if datetime.now() - ban_list[ip] > BAN_DURATION:
                unban_ip(ip)

        time.sleep(0.1)

if __name__ == "__main__":
    try:
        monitor()
    except KeyboardInterrupt:
        print("\n[!] Exiting Ghost-Sentinel Mk1.")
