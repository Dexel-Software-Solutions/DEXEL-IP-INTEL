# 🌐 DEXEL IP INTEL

Advanced Terminal-Based IP Intelligence & Risk Analysis Tool
Developed By **Demiyan Dissanayake**
Powered By **Dexel Software Solutions**

---

## 🚀 Overview

DEXEL IP INTEL is a powerful terminal-based IP intelligence tool built using Python. It collects detailed information about any public IP address and generates a structured intelligence report.

This tool is ideal for:

* Cyber Security Students
* Ethical Hackers
* Network Engineers
* IT Professionals
* Security Researchers

---

## 🔥 Features

* Full IP Geolocation Data
* ISP & Organization Details
* Reverse DNS Lookup
* WHOIS Organization Lookup
* Common Port Scanning
* Subnet Information (/24)
* Risk Score Calculation
* Google Maps Location Link
* Export Report as TXT
* Export Report as JSON
* Clean Terminal UI with Banner

---

## 🛠 Technologies Used

* Python 3
* requests
* socket
* python-whois
* colorama
* pyfiglet
* ip-api.com (IP Data API)

---

## 📦 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/dexel-ip-intel.git
cd dexel-ip-intel
```

### 2️⃣ Install Dependencies

```bash
pip install requests python-whois colorama pyfiglet
```

---

## ▶️ Usage

Run the tool:

```bash
python dexel_ip_intel.py
```

Menu Options:

```
1. Scan IP
2. Exit
```

Enter a valid public IP address (Example: 8.8.8.8)

---

## 📊 Example Output

```
[ FULL IP INTELLIGENCE REPORT ]
------------------------------------------------------------
IP              : 8.8.8.8
Country         : United States
Region          : California
City            : Mountain View
ISP             : Google LLC
Org             : Google LLC
AS              : AS15169 Google LLC
Latitude        : 37.4056
Longitude       : -122.0775
Timezone        : America/Los_Angeles
ReverseDNS      : dns.google
WHOIS Org       : Google LLC
Open Ports      : [53, 443]
Subnet          : 8.8.8.0/24
Risk Score      : 30
Google Maps     : https://www.google.com/maps?q=37.4056,-122.0775
------------------------------------------------------------
```

---

## 🧠 Risk Score Logic

Risk score is calculated based on:

* More than 3 open common ports → +40
* Hosting / Cloud ISP detected → +30
* RDP Port (3389) open → +30

Maximum Risk Score = 100

---

## 📁 Export Options

After scanning an IP address:

* Save Report as TXT → report_<IP>.txt
* Save Report as JSON → report_<IP>.json

---

## ⚠️ Important Notes

* Works only with Public IP addresses.
* Private IPs (192.168.x.x, 10.x.x.x, etc.) will not return valid results.
* Port scanning checks common ports only.
* Geolocation accuracy depends on ISP data.

---

## 📜 Disclaimer

This tool is created strictly for:

* Educational purposes
* Ethical security testing
* Network analysis

Do NOT use this tool for illegal activities.

The developer is not responsible for any misuse of this software.

---

## 👨‍💻 Developer

Developer Name: Demiyan Dissanayake
Organization: Dexel Software Solutions
GitHub Support: [https://github.com/Dexel-Software-Solutions](https://github.com/Dexel-Software-Solutions)

---

## ⭐ Support The Project

If you like this project:

* Star the repository
* Fork the project
* Share with others

---

# 🔐 DEXEL IP INTEL

Professional • Powerful • Precise
