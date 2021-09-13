import time
import sys

# my imports
import constants
from crawler import Crawler


def download():
    crawler = Crawler(sys.argv[1])    
    for sign in constants.SIGNS:
        print("[SIGN] " + sign)
        url = constants.URL
        url = url.replace(constants.SIGN, sign)
        for page_number in range(constants.NUMBER_OF_PAGES):
            print("page: " + str(page_number))
            if (page_number + 1) == 1:
                crawler.fetch(constants.BASE_URL.replace(constants.SIGN, sign), sign)
            else:
                crawler.fetch(url.replace(constants.PAGE_NUMBER, str(page_number + 1)), sign)
            time.sleep(1)


# Main method
def main():
    if (len(sys.argv) != 2):
        print("Please provide only a single filename as the args.")
        sys.exit(-1)
    print("\nStarting Download...")
    print("\tUsing file: " + sys.argv[1])
    download()
    print("\nDownload complete, and written to file: " + sys.argv[1])
    sys.exit(0)


# Call to main method
if __name__ == "__main__":
    main()
