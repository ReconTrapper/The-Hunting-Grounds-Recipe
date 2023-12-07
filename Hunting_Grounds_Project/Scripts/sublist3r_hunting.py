import subprocess
import json
import socket

def sublist3r_scan(target_domain, output_file):
    command = f"sublist3r -d {target_domain} -o {output_file}"
    subprocess.run(command, shell=True)

def get_ip_addresses(subdomains):
    ip_addresses = {}
    for subdomain in subdomains:
        try:
            ip_address = socket.gethostbyname(subdomain)
            ip_addresses[subdomain] = ip_address
        except socket.error as e:
            print(f"Error resolving IP address for {subdomain}: {e}")
    return ip_addresses

def save_to_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=2)

def main():
    # Customize these variables
    target_domain = "example.com"
    output_file_sublist3r = "subdomains_sublist3r.txt"
    output_file_ip_addresses = "ip_addresses.json"

    # Subdomain Enumeration
    print("[*] Starting Sublist3r scan...")
    sublist3r_scan(target_domain, output_file_sublist3r)
    print(f"[+] Sublist3r scan completed. Subdomains saved to: {output_file_sublist3r}")

    # Read subdomains from Sublist3r output
    with open(output_file_sublist3r, 'r') as sublist3r_file:
        subdomains = [line.strip() for line in sublist3r_file if line.strip()]

    # Get IP addresses for subdomains
    ip_addresses = get_ip_addresses(subdomains)
    print(f"[+] IP addresses resolved for subdomains. Data saved to: {output_file_ip_addresses}")

    # Save results to JSON files
    save_to_json({"subdomains": subdomains, "ip_addresses": ip_addresses}, output_file_ip_addresses)

if __name__ == "__main__":
    main()

