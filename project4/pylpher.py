import argparse
import os

def main():
    parser=argparse.ArgumentParser(description="Pylpher")
    parser.add_argument("DIR", help="Directory to search", default=".", nargs="?")
    parser.add_argument("-r", help="Recursive search", action="store_true")
    group1=parser.add_mutually_exclusive_group()
    group1.add_argument("-f", metavar="filename", help="Filenames to search for (comma-separated)")
    group1.add_argument("-F", metavar="filelist", help="Filenames to search for (wordlist)")
    group2=parser.add_mutually_exclusive_group()
    group2.add_argument("-x", "--extname", help="Extensions to search for (comma-separated)")
    group2.add_argument("-X", "--extlist", help="Extensions to search for (wordlist)")
    group3=parser.add_mutually_exclusive_group()
    group3.add_argument("-s", "--strname", help="Strings to search for (comma-separated)")
    group3.add_argument("-S", "--strlist", help="Strings to search for (wordlist)")
    args=parser.parse_args()

    if args.f:
        filenames=[args.f]
    elif args.F:
        with open(args.F, encoding="utf-8") as file:
            filenames=file.read().split()
    else:
        filenames=["web.config"]

    if args.r:
        for (dirpaths, dirnames, files) in os.walk(args.DIR):
            print(f"Searching: {dirpaths}")
            for filename in files:
                print(f"\t{filename}")
    else:
        for entry in os.listdir(args.DIR):
            print(entry)

if __name__=="__main__":
    main()
