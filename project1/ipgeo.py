''' IP ownership, geolocation '''
import argparse
import ipaddress
import json
import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = "https://api.ipgeolocation.io/ipgeo"

def get_addr(ips):
    ''' Get address(es) '''
    ip_list = []
    try:
        for line in ips:
            for ip_addr in ipaddress.ip_network(line.strip()):
                ip_list.append(ip_addr)
        return ip_list
    except ValueError:
        print("Not a valid IP address or subnet")
        sys.exit(1)

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
        #file = open(args.inFile, encoding = 'utf8')
        with open(args.inFile, encoding = "utf8") as file:
            ips = get_addr(file.readlines())
    else:
        ips = [""]

    for ip_addr in ips:
        response = requests.get(API_URL + "?apiKey=" + API_KEY + "&ip=" \
                                + str(ip_addr) + "&fields=geo,organization")
        parsed = json.loads(response.text)
        print(json.dumps(parsed, indent = 4, sort_keys = True))

if __name__ == "__main__":
    main()
