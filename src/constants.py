# This file contains the constants used by the driver.py and 
# crawler.py programs.


SIGNS = [
        "aquarius",
        "pisces",
        "aries",
        "taurus",
        "gemini",
        "cancer",
        "leo",
        "virgo",
        "libra",
        "scorpio",
        "sagittarius",
        "capricorn"
        ]

# URLs contain replacable symbols for dynamic url fetching
URL = "https://mystarshoroscopes.com/category/${SIGN}/${SIGN}-daily-horoscope/page/${PAGE_NUMBER}/"
BASE_URL = "https://mystarshoroscopes.com/category/${SIGN}/${SIGN}-daily-horoscope"
SIGN = "${SIGN}"
PAGE_NUMBER = "${PAGE_NUMBER}"

# number of pages deep to go in scraping history
NUMBER_OF_PAGES = 100
