''' IP ownership, geolocation '''
import argparse
import ipaddress
import json
import os
import sys
import requests
from dotenv import load_dotenv

if load_dotenv():
    API_KEY = os.getenv("API_KEY")
else:
    print("No environment file found, exiting!")
    sys.exit(1)

API_URL = "https://api.ipgeolocation.io/ipgeo"

def get_addr(ips):
    ''' Get address(es) '''
    ip_list = []
    for line in ips:
        try:
            for ip_addr in ipaddress.ip_network(line):
                ip_list.append(ip_addr)
        except ValueError:
            print(f"{line} is not a valid IP address or subnet")
    return ip_list

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description = "Get IP ownership and geolocation info")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("IP", help = "IP address (CIDR supported) to look up", nargs = "?")
    group.add_argument("-i", "--inFile", help = "File containing IP addresses or CIDR blocks")
    args = parser.parse_args()

    if args.IP:
        ips = get_addr([args.IP])
    elif args.inFile:
        try:
            with open(args.inFile, encoding = "utf8") as file:
                ips = get_addr(file.read().split())
        except FileNotFoundError:
            print(f"{args.inFile} bad file")
            sys.exit(1)
    else:
        ips = [""]

    for ip_addr in ips:
        try:
            response = requests.get(API_URL + "?apiKey=" + API_KEY + "&ip=" \
                                + str(ip_addr) + "&fields=geo,organization", timeout=5)
            parsed = json.loads(response.text)
            print(json.dumps(parsed, indent = 4, sort_keys = True))
        except requests.exceptions.ConnectionError:
            print(f"Error with IP: {ip_addr}. Is this IP valid? Do you have network connection?")

if __name__ == "__main__":
    main()
