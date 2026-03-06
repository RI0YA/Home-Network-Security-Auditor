#  NetGuard Pro: Automated Network Security Auditor
**Developed by Riya Gupta | PG-DASSD, CDAC Hyderabad**

##  Overview
NetGuard Pro is a professional-grade vulnerability assessment tool built in Python. It automates complex Nmap scanning phases into a streamlined workflow, identifying live assets and mapping them against common security risks.

##  Key Features
- **Deep Service Fingerprinting:** Utilizes Nmap's engine to identify exact software versions on open ports.
- **Automated Risk Mapping:** Integrated logic to flag high-risk services like SMB (445) and unencrypted HTTP (80).
- **Portable Deployment:** Compiled into a standalone `.exe` using PyInstaller for universal Windows execution.
- **Automated Reporting:** Generates timestamped security audit logs for compliance and documentation.

## Technical Methodology
The auditor follows a multi-phase scanning approach:
1. **Asset Discovery:** ICMP echo requests to identify active hosts on the subnet.
2. **Service Discovery:** TCP SYN scanning to locate open ports.
3. **Vulnerability Analysis:** NSE (Nmap Scripting Engine) integration for version detection and risk assessment.

## 📂 Project Structure
- **/src**: Python source code (`main.py`).
- **/dist**: Compiled standalone executable (`NetGuard_Auditor_Pro.exe`).
- **/build**: Intermediate build files and metadata.

## ⚙️ Requirements
- Windows 10/11
- [Nmap 7.98+](https://nmap.org/download.html) (Core Engine)
