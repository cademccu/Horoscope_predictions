import time

# my imports
import constants
import crawler


def download():
    
    for sign in constants.SIGNS:
        url = constants.URL
        url = url.replace(constants.SIGN, sign)
        for page_number in range(constants.NUMBER_OF_PAGES):
            if (page_number + 1) == 1:
                print(constants.BASE_URL.replace(constants.SIGN, sign))
            else:
                print(url.replace(constants.PAGE_NUMBER, str(page_number + 1)))


# Main method
def main():
    download()


# Call to main method
if __name__ == "__main__":
    main()
