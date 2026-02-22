#!/usr/bin/env python3
import requests
import sys
import socket
import json
import argparse
import time
import os
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init(autoreset=True)

class BalkrishnaISPFinder:
    def __init__(self):
        # API fields optimized for your specific requirements
        self.api_url = "http://ip-api.com/json/{}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query"

    def banner(self):
        """Stylish ASCII Banner for Termux/Linux"""
        os.system('clear' if os.name == 'posix' else 'cls')
        banner_text = f"""
{Fore.RED}{Style.BRIGHT} 

    ██████╗  █████╗ ██╗     ██╗  ██╗██████╗ ██╗███████╗██╗  ██╗███╗   ██╗ █████╗ 
    ██╔══██╗██╔══██╗██║     ██║ ██╔╝██╔══██╗██║██╔════╝██║  ██║████╗  ██║██╔══██╗
    ██████╔╝███████║██║     █████╔╝ ██████╔╝██║███████╗███████║██╔██╗ ██║███████║
    ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══██╗██║╚════██║██╔══██║██║╚██╗██║██╔══██║
    ██████╔╝██║  ██║███████╗██║  ██╗██║  ██╗██║███████║██║  ██║██║ ╚████║██║  ██║
    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
{Fore.YELLOW}               🔥 ULTIMATE IP & ISP INTELLIGENCE TOOL v4.0 🔥
{Fore.CYAN}                 Created by: Balkrishna | Authorized Pentest
        """
        print(banner_text)
        print(f"{Fore.WHITE}[{datetime.now().strftime('%H:%M:%S')}] {Fore.GREEN}System Online. Target analysis ready...")

    def scan_ip(self, ip):
        self.banner()
        print(f"\n{Fore.YELLOW}🔍 Analyzing Target: {Fore.WHITE}{ip}")
        print(f"{Fore.BLUE}{'='*70}")

        try:
            # Fetching data from ip-api
            response = requests.get(self.api_url.format(ip), timeout=10)
            data = response.json()

            if data.get('status') == 'fail':
                print(f"{Fore.RED}❌ Error: {data.get('message', 'Invalid IP address provided')}")
                return

            # Structured Data Output
            info_map = [
                ("Query/IP", "query"), ("Status", "status"), ("ISP", "isp"),
                ("Organization", "org"), ("AS/ASN", "as"), ("Country", "country"),
                ("Country Code", "countryCode"), ("Region Name", "regionName"),
                ("Region Code", "region"), ("City", "city"), ("Zip Code", "zip"),
                ("Timezone", "timezone"), ("Latitude", "lat"), ("Longitude", "lon")
            ]

            for label, key in info_map:
                value = data.get(key, "N/A")
                print(f"{Fore.CYAN}{label:<18} : {Fore.WHITE}{value}")

            # Accurate Google Maps Link
            lat, lon = data.get('lat'), data.get('lon')
            if lat and lon:
                maps_url = f"https://www.google.com/maps?q={lat},{lon}"
                print(f"{Fore.GREEN}{'Google Maps':<18} : {Fore.YELLOW}{maps_url}")

        except Exception as e:
            print(f"{Fore.RED}❌ Connection Error: {str(e)}")

        print(f"{Fore.BLUE}{'='*70}")
        print(f"{Fore.MAGENTA}✅ Reconnaissance Complete!\n")

def main():
    tool = BalkrishnaISPFinder()
    parser = argparse.ArgumentParser(description='Balkrishna ISP Finder - IP Recon Tool')
    parser.add_argument('target', nargs='?', help='Target IP address')
    args = parser.parse_args()

    if args.target:
        tool.scan_ip(args.target)
    else:
        tool.banner()
        target_ip = input(f"{Fore.YELLOW}Enter Target IP to Scan: {Fore.WHITE}")
        if target_ip.strip():
            tool.scan_ip(target_ip)
        else:
            print(Fore.RED + "No IP entered. Exiting...")

if __name__ == "__main__":
    main()