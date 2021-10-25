import argparse
import requests
import os
from dotenv import load_dotenv
import json
import ipaddress
import sys

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = "https://api.ipgeolocation.io/ipgeo"

def getAddr(ips):
    ipList = []
    try:
        for line in ips:
            for ip in ipaddress.ip_network(line.strip()):
                ipList.append(ip)
        return ipList
    except ValueError:
        print("Not a valid IP address or subnet")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description = "Get IP ownership and geolocation info")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("IP", help = "IP address (CIDR supported) to look up (if omitted, info from this machine will be returned)", nargs = "?")
    group.add_argument("-i", "--inFile", help = "File containing IP addresses or CIDR blocks")
    args = parser.parse_args()

    if args.IP:
        ips = getAddr([args.IP])
    elif args.inFile:
        file = open(args.inFile)
        ips = getAddr(file.readlines())
    else:
        ips = [""]

    for ip in ips:
        response = requests.get(API_URL + "?apiKey=" + API_KEY + "&ip=" + str(ip) + "&fields=geo,organization")
        parsed = json.loads(response.text)
        print(json.dumps(parsed, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()
