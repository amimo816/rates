# PhantomJs needed or other browser

from selenium import webdriver
import csv
import time

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


print(rates)
with open('test.csv', 'w', newline='') as fp:
    csvWr = csv.writer(fp, delimiter=',')
    for key in rates:
        if DEBUG:
            print("Period: " + key + " Rate: " + rates[key][0] + " Date: " + rates[key][1])
        row = key + "," + rates[key][0] + "," + rates[key][1]
        csvWr.writerow(row)
test = str(rates["3 mån"][0])
print(test)
