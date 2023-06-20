''' Header security checker '''
import argparse
import requests
from colorama import Fore, Style

tests = [
    {"name":"Strict-Transport-Security", "skippable":True, "printable":False},
    {"name":"Content-Security-Policy", "skippable":False, "printable":False},
    {"name":"X-Frame-Options", "skippable":False, "printable":False},
    {"name":"Server", "skippable":False, "printable":True}
]

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description = "Check URLs for common header security issues")
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument("URL", help = "URL to query", nargs = "?")
    group.add_argument("-i", "--inFile", help = "File containing URLs")
    args = parser.parse_args()

    if args.URL:
        urls = [args.URL]
    elif args.inFile:
        with open(args.inFile, encoding = 'utf8') as file:
            urls = file.read().split()

    if len(urls) > 0:
        for url in urls:
            try:
                response = requests.get(url, timeout=5)
                print(url + ":")
                for test in tests:
                    if test["skippable"] is True and url[:5] != "https":
                        print(f"\t{test['name']:<35} {Fore.YELLOW}SKIP (N/A){Style.RESET_ALL}")
                    elif test["printable"] is True:
                        if test["name"] in response.headers:
                            print(f"\t{test['name']:<35} {response.headers[test['name']]}")
                    else:
                        if test["name"] in response.headers:
                            print(f"\t{test['name']:<35} {Fore.GREEN}PASSED{Style.RESET_ALL}")
                        else:
                            print(f"\t{test['name']:<35} {Fore.RED}FAILED{Style.RESET_ALL}")
            except requests.exceptions.RequestException:
                print(f"{Fore.RED}Issue with", url, f"{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}No URLs to check!{Style.RESET_ALL}")

    print("Done!")

if __name__ == "__main__":
    main()
