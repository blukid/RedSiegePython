''' Header security checker '''
import argparse
import requests
from colorama import Fore, Style

tests = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options"
]

def check_urls(urls):
    ''' check each url is HTTPS, add to list if so '''
    url_list = []
    for url in urls:
        if url[:5] != "https":
            print(url + " is not an HTTPS URL, ignoring!")
        else:
            url_list.append(url)
    return url_list

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description = "Check URLs for common header security issues")
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument("URL", help = "URL to query", nargs = "?")
    group.add_argument("-i", "--inFile", help = "File containing URLs")
    args = parser.parse_args()

    if args.URL:
        urls = check_urls([args.URL])
    elif args.inFile:
        with open(args.inFile, encoding = 'utf8') as file:
            urls = check_urls(file.readlines())

    if len(urls) > 0:
        for url in urls:
            try:
                response = requests.get(url)
                #print(response.headers)
                print(url + ":")
                for test in tests:
                    try:
                        if response.headers[test]:
                            print(f"\t{test:<35} {Fore.GREEN}PASSED{Style.RESET_ALL}")
                    except KeyError:
                        print(f"\t{test:<35} {Fore.RED}FAILED{Style.RESET_ALL}")
                        continue
            except Exception as xcpt:
                print(f"Exception: {type(xcpt).__name__}")
                print(f"Exception message: {xcpt}")

    print("\nDone!")

if __name__ == "__main__":
    main()
