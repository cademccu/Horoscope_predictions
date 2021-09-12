

from crawler import Crawler
import constants


crawler = Crawler("test.csv")

crawler.fetch("https://mystarshoroscopes.com/category/aquarius/aquarius-daily-horoscope/")
