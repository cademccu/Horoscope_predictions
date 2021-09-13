from bs4 import BeautifulSoup as BS
import time
import requests
import datetime

# my constants
import constants

class Crawler:
    # This class uses the requests library to fetch a webpage,
    # then uses beautiful soup to parse the data, and append
    # to a csv file for use later. The file is kept open
    # to avoid costly I/O resources, and closed upon sys.exit()
    def __init__(self, filename):
        self.file = None

        try:
            self.file = open(filename, 'a')
        except IOError as io:
            print("[ERROR] Error occured when opening file:")
            print(io)
            sys.exit(0)

    # clean up resources and close file.
    def __del__(self):
        self.file.close()

    def writefile(self, sign, date, value):
        # Logs the data, and writes the data to the CSV file in a readable format.
        self.file.write(sign + "," + date + ",\"" + value + "\"\n")
        print("\t[CSV]: " + sign + "," + date + "," + value[:20])



    def fetch(self, URL, sign):
        # get the page at the url specified and then write 
        # the subsequent data to the csv file.
        page = requests.get(URL)
        soup = BS(page.content, "html.parser")

        # probably a clearer more dynamic way to do this but results are constant
        texts = soup.find_all(class_ = "entry-content")
        dates = soup.find_all(class_ = "entry-header")

        for i in range(len(texts)):
            textstr = texts[i].find('p').get_text()
            date = dates[i].find('p').find('time').get_text().split()
            dateobj = datetime.datetime.strptime(date[0], "%B")
            datestr = date[1].replace(",","").zfill(2) + "/" + str(dateobj.month).zfill(2) + "/" + date[2]
            self.writefile(sign, datestr, textstr)
            

