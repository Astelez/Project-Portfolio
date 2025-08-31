# NIDS on Raspberry Pi — Suricata

**Goal**: Deploy Suricata on a Raspberry Pi to monitor a test network, write custom rules, and generate/triage alerts for common attacks (port scans, brute force, ARP spoofing).

## Architecture
- Raspberry Pi (sensor) → mirrored/monitored traffic
- Attacker VM (Kali) → Nmap, Hydra
- Victim VM (Linux/Windows)
- Log view: `eve.json` → Kibana/ELK (optional)

## Setup (TL;DR)
```bash
# RPi
sudo apt update && sudo apt install -y suricata jq
sudo suricata -V
# Example: copy custom rules
sudo cp rules/local.rules /etc/suricata/rules/local.rules
# Validate & start
sudo suricata -T -c /etc/suricata/suricata.yaml
sudo systemctl enable --now suricata
```

## Test Scenarios
- **Port Scan**: `nmap -sS <victim-ip>`  
- **SSH Brute Force**: `hydra -l test -P rockyou.txt ssh://<victim-ip>`  
- **ARP Spoof** (lab-only): `arpspoof -t <victim-ip> <gateway-ip>`

## Results & Screenshots
Add screenshots from Kibana or `jq` filtered `eve.json` here.
- `artifacts/alerts-portscan.png`
- `artifacts/alerts-bruteforce.png`

## Custom Rules
See `rules/local.rules` for examples. Tune SID ranges and `rev` properly.

## What I Learned (fill this in)
- TODO: packet capture tips
- TODO: rule tuning vs noise
- TODO: mapping alerts to MITRE ATT&CK

## Next Steps
- Forward logs to ELK/Splunk
- Add Zeek for richer metadata