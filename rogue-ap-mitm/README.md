# Rogue Access Point + MITM (Kali Lab Only)

**Goal**: Build a rogue Wi‑Fi AP in a closed lab, capture traffic from a test client, analyze credentials/cookies, and document **defenses**.

> **Safety**: Use **only** with your own devices in a controlled lab. Never transmit or store real credentials.

## Architecture
- Kali host with wireless adapter (AP mode)
- Test client VM (Linux/Windows) connecting to the rogue AP
- Optional transparent proxy or DNS spoof for demo

## Setup (Outline)
```bash
sudo apt update && sudo apt install -y hostapd dnsmasq tcpdump python3-pip
# Configure hostapd & dnsmasq (see configs/)
sudo systemctl enable --now hostapd dnsmasq
# Capture traffic
sudo tcpdump -i wlan0 -w artifacts/capture.pcapng
```

## Demo Flow
1. Start AP, verify client association.
2. Browse to a non‑HTTPS test site in the lab or an intentionally insecure local web app.
3. Capture traffic; export PCAP; run parsing script.
4. Document what worked and why defenses matter.

## Deliverables
- PCAP(s) in `artifacts/` (gitignored by default)
- `scripts/parse_credentials.py` (example starter below)
- Screenshots of association, traffic, and parsed results
- **Defense section**: WPA3, HTTPS-only, HSTS, VPN, EAP‑TLS, user education

## What I Learned
- TODO: radio/driver gotchas
- TODO: limits of passive vs active MITM
- TODO: why modern defenses help