import nmap
import datetime
import os
import sys

def generate_pro_report():
    nm = nmap.PortScanner()
    print("NETGUARD PRO: AUTOMATED SECURITY AUDITOR")
    print("-" * 45)
    
    target = input("Enter Network Range (e.g., 192.168.1.0/24): ")
    print(f"[*] Starting Multi-Phase Scan on {target}...")

    try:
        # Phase 1: Aggressive Service Discovery & OS Fingerprinting
        # Arguments: -A (Aggressive), -T4 (Speed), -Pn (Treat all hosts as online)
        nm.scan(hosts=target, arguments='-A -T4 -Pn')
        
        filename = f"Security_Audit_{datetime.date.today()}.txt"
        with open(filename, "w") as f:
            f.write(f"NETWORK SECURITY ASSESSMENT REPORT\n")
            f.write(f"Date: {datetime.date.today()} | Tool: NetGuard Pro\n")
            f.write("="*60 + "\n")

            for host in nm.all_hosts():
                f.write(f"\n[!] AUDIT TARGET: {host}\n")
                f.write(f"    State: {nm[host].state()}\n")
                
                # OS Detection Logic
                if 'osmatch' in nm[host]:
                    f.write(f"    Detected OS: {nm[host]['osmatch'][0]['name']}\n")

                for proto in nm[host].all_protocols():
                    ports = nm[host][proto].keys()
                    for port in ports:
                        service = nm[host][proto][port]['name']
                        version = nm[host][proto][port]['version']
                        f.write(f"    -> Port {port}: {service} ({version})\n")
                        
                        # Vulnerability Mapping (The "Edge")
                        if port == 445: f.write("       [!] CRITICAL: SMB Vulnerability Risk. Mitigation: Disable SMBv1.\n")
                        if port == 80: f.write("       [!] RISK: Cleartext HTTP found. Use HTTPS (443).\n")

        print(f"\n[SUCCESS] Professional Report saved as: {filename}")
    except Exception as e:
        print(f"[ERROR] Scan failed. Ensure Nmap is installed: {e}")

if __name__ == "__main__":
    generate_pro_report()