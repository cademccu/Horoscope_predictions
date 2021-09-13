

from crawler import Crawler
import constants


#crawler = Crawler("test.csv")

#crawler.fetch("https://mystarshoroscopes.com/category/aquarius/aquarius-daily-horoscope/")

import requests

page = requests.get("https://mystarshoroscopes.com/category/aquarius/aquarius-daily-horoscope/")

print("STATUS:", str(page.status_code))

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

import datetime

#for p in soup.find_all('p'):
#    print(p.get_text())
#    print("-----------------------------")


for div in soup.find_all(class_ = "entry-content"):
    print(div.find('p').get_text())
    print("-----------------------------")

print(len(soup.find_all(class_ = "entry-content")))



for div in soup.find_all(class_ = "entry-header"):
    date = div.find('p').find('time').get_text().split()
    dateobj = datetime.datetime.strptime(date[0], "%B")
    print("day: " + date[1].replace(",", ""))
    print("month: " + str(dateobj.month))
    print("year: " + date[2])
    datestr = date[1].replace(",","").zfill(2) + "/" + str(dateobj.month).zfill(2) + "/" + date[2]
    print(datestr)
    # day / month / year ?
    # month / day / year ? 
    print("-----------------------------")

print(len(soup.find_all(class_ = "entry-header")))
