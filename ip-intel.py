import requests
import socket
import json
import sys
import re
import whois
from datetime import datetime
from colorama import Fore, Style, init
import pyfiglet

init(autoreset=True)

# =========================
# Banner
# =========================
def banner():
    print(Fore.CYAN + pyfiglet.figlet_format("DEXEL IP INTEL"))
    print(Fore.GREEN + "Developer : Demiyan Dissanayake")
    print(Fore.GREEN + "Powered By : Dexel Software Solutions")
    print(Fore.YELLOW + "-" * 70)

# =========================
# Validate IP
# =========================
def validate_ip(ip):
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return pattern.match(ip)

# =========================
# Reverse DNS
# =========================
def reverse_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "N/A"

# =========================
# WHOIS Lookup
# =========================
def whois_lookup(ip):
    try:
        w = whois.whois(ip)
        return str(w.org) if w.org else "N/A"
    except:
        return "N/A"

# =========================
# Port Scanner
# =========================
def port_scan(ip):
    common_ports = [21,22,23,25,53,80,110,139,143,443,445,3389]
    open_ports = []
    print(Fore.CYAN + "\nScanning Common Ports...")
    for port in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        s.close()
    return open_ports

# =========================
# Subnet Info
# =========================
def subnet_info(ip):
    parts = ip.split(".")
    return f"{parts[0]}.{parts[1]}.{parts[2]}.0/24"

# =========================
# Risk Score
# =========================
def risk_score(open_ports, isp):
    score = 0
    if len(open_ports) > 3:
        score += 40
    if "hosting" in isp.lower() or "cloud" in isp.lower():
        score += 30
    if 3389 in open_ports:
        score += 30
    return min(score,100)

# =========================
# Get IP Details
# =========================
def get_ip_details(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()

    if data["status"] != "success":
        print(Fore.RED + "Invalid or Private IP!")
        return None

    open_ports = port_scan(ip)
    rdns = reverse_dns(ip)
    whois_org = whois_lookup(ip)
    subnet = subnet_info(ip)
    risk = risk_score(open_ports, data.get("isp",""))

    result = {
        "IP": ip,
        "Country": data.get("country"),
        "Region": data.get("regionName"),
        "City": data.get("city"),
        "ISP": data.get("isp"),
        "Org": data.get("org"),
        "AS": data.get("as"),
        "Latitude": data.get("lat"),
        "Longitude": data.get("lon"),
        "Timezone": data.get("timezone"),
        "ReverseDNS": rdns,
        "WHOIS Org": whois_org,
        "Open Ports": open_ports,
        "Subnet": subnet,
        "Risk Score": risk,
        "Google Maps": f"https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}"
    }

    display_result(result)
    return result

# =========================
# Display Result
# =========================
def display_result(data):
    print(Fore.CYAN + "\n[ FULL IP INTELLIGENCE REPORT ]")
    print(Fore.YELLOW + "-" * 60)
    for key, value in data.items():
        print(Fore.GREEN + f"{key:<15} : {value}")
    print(Fore.YELLOW + "-" * 60)

# =========================
# Save TXT
# =========================
def save_txt(data):
    filename = f"report_{data['IP']}.txt"
    with open(filename,"w") as f:
        for k,v in data.items():
            f.write(f"{k} : {v}\n")
    print(Fore.GREEN + f"Report saved as {filename}")

# =========================
# Save JSON
# =========================
def save_json(data):
    filename = f"report_{data['IP']}.json"
    with open(filename,"w") as f:
        json.dump(data,f,indent=4)
    print(Fore.GREEN + f"JSON saved as {filename}")

# =========================
# Menu
# =========================
def main():
    banner()

    while True:
        print(Fore.CYAN + "\n1. Scan IP")
        print("2. Exit")

        choice = input(Fore.YELLOW + "\nSelect Option: ")

        if choice == "1":
            ip = input(Fore.CYAN + "Enter IP Address: ")

            if not validate_ip(ip):
                print(Fore.RED + "Invalid IP Format!")
                continue

            result = get_ip_details(ip)

            if result:
                print("\n1. Save TXT")
                print("2. Save JSON")
                print("3. Back")
                sub = input("Select Option: ")

                if sub == "1":
                    save_txt(result)
                elif sub == "2":
                    save_json(result)

        elif choice == "2":
            print(Fore.RED + "Exiting...")
            sys.exit()

        else:
            print(Fore.RED + "Invalid Choice!")

if __name__ == "__main__":
    main()