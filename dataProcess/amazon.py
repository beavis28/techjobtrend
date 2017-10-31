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
output_data = []

#print(soup.find_all('item')[0]('itemlinks').prettify())
for item in soup.find_all('item'):
  output_data.append({'title': item.title.text, 'image': item.mediumimage.url.text, 'url': item.url.text})

with open(join('result', 'amazon_data.json'), 'w') as outfile:
    json.dump(output_data, outfile)
