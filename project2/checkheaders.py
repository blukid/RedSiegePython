''' Header security checker '''
import argparse
import requests

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
        file = open(args.inFile, encoding = 'utf8')
        urls = check_urls(file.readlines())

    print("Starting Strict-Transport-Security test\n")
    if len(urls) > 0:
        try:
            for url in urls:
                response = requests.get(url)
                #print(response.headers)
                if response.headers["Strict-Transport-Security"]:
                    print(url + " passed!")
        except KeyError:
            print(url + " failed!")
        except Exception as xcpt:
            print(f"Exception: {type(xcpt).__name__}")
            print(f"Exception message: {xcpt}")

    print("\nDone!")

if __name__ == "__main__":
    main()
