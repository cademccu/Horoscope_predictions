from bs4 import BeautifulSoup
import time
import requests


import constants

class Crawler:
    # This class uses the requests library to fetch a webpage,
    # then uses beautiful soup to parse the data, and append
    # to a csv file for use later.
    def __init__(self, filename):
        self.filename = filename


    




    def fetch(self, URL):
        # get the page at the url specified and then write 
        # the subsequent data to the csv file.
        pass
