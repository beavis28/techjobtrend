import bottlenose
from bs4 import BeautifulSoup
import lxml.etree as etree  
from os.path import isfile, join
import json

ACCESS_KEY = "AKIAIJWGVA4XGB6P6OQA"
SECRET_ACCESS_KEY = "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"
ASSOCIATE_TAG = "beavis2809-20"
 
amazon = bottlenose.Amazon(ACCESS_KEY, SECRET_ACCESS_KEY, ASSOCIATE_TAG)
response = amazon.ItemSearch(Keywords="javascript", SearchIndex="KindleStore", ResponseGroup="Images, ItemAttributes, Offers")
soup = BeautifulSoup(response,"lxml")


with open(join('result', 'amazon.json'), 'w') as outfile:
    json.dump(soup.find('items').prettify(), outfile)
#print(soup.find('items').prettify())
