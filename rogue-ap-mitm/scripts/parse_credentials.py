#!/usr/bin/env python3
"""Minimal PCAP parser for lab demos.

- Reads a PCAP/PCAPNG and searches for naive credential patterns (HTTP forms).
- For educational use in a closed lab only.
"""
import sys, re
from pathlib import Path

def parse_http_forms(pcap_bytes: bytes):
    # Extremely naive approach for demo; replace with pyshark/scapy for real parsing.
    # Look for 'username=' or 'password=' in raw payloads.
    findings = []
    for m in re.finditer(rb'(username|user|login)[^\n\r]{{0,50}}(=|:)[^\n\r]{{0,200}}|(password|pass)[^\n\r]{{0,50}}(=|:)[^\n\r]{{0,200}}', pcap_bytes, re.IGNORECASE):
        s = m.group(0)
        # Truncate for display
        findings.append(s[:120])
    return findings

def main():
    if len(sys.argv) < 2:
        print("Usage: parse_credentials.py <capture.pcapng>")
        sys.exit(1)
    p = Path(sys.argv[1])
    data = p.read_bytes()
    hits = parse_http_forms(data)
    if not hits:
        print("No naive credential patterns found (good!).")
    else:
        print(f"Potential matches (raw, truncated): {len(hits)}")
        for i, h in enumerate(hits, 1):
            try:
                print(f"[{i}] {h.decode('utf-8', 'ignore')}")
            except:
                print(f"[{i}] <binary>")

if __name__ == "__main__":
    main()