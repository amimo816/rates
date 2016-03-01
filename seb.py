# PhantomJs needed or other browser

from selenium import webdriver
import csv
import time
import json

DEBUG = False

browser = webdriver.PhantomJS()
#browser = webdriver.Firefox()
rates = {}

webPage = ('http://seb.se/pow/apps/upplaningsranta/default.aspx')
browser.get(webPage)
searchCriteria = "//td"
searchResult = browser.find_elements_by_xpath(searchCriteria)

# SearchResults =
# contract length, rate, date, contract length, rate, date
for i in range(0,len(searchResult),3):
    rates[searchResult[i].text] = [searchResult[i+1].text, searchResult[i+2].text]

if DEBUG:
    print("Rates dict is: " + str(rates))

with open('test.json', 'a') as fp:
    json.dump(rates,fp)

    if DEBUG:
        for key in rates:
            print("Period: " + key + " Rate: " + rates[key][0] + " Date: " + rates[key][1])


