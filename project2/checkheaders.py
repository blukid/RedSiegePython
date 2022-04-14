import argparse
import requests
import sys

def checkURLs(urls):
    urlList = []
    for url in urls:
        if url[:5] != "https":
            print(url + " is not an HTTPS URL, ignoring!")
    else:
        urlList.append(url)
    return urlList

def main():
    parser = argparse.ArgumentParser(description = "Check URLs for common security issues with headers")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("URL", help = "URL to query", nargs = "?")
    group.add_argument("-i", "--inFile", help = "File containing URLs")
    args = parser.parse_args()

    if args.URL:
        urls = checkURLs([args.URL])
    elif args.inFile:
        file = open(args.inFile)
        urls = checkURLs(file.readlines())

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
        except Exception as e:
            print("Exception: {}".format(type(e).__name__))
            print("Exception message: {}".format(e))

    print("\nDone!")

if __name__ == "__main__":
    main()
