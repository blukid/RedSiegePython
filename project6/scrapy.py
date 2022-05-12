import requests
import argparse

def parse_url(url):
    return url if url[:4]=="http" else "https://"+url

def main():
    ''' main '''
    parser=argparse.ArgumentParser(description="Scrape web site for keywords")
    parser.add_argument("URL", help="URL to scrape from")
    parser.add_argument("-o", "--output", help="File to output to")
    args=parser.parse_args()

    url=parse_url(args.URL)
    print(url)
    resp=requests.get(url)
    print(resp)

if __name__=="__main__":
    main()
