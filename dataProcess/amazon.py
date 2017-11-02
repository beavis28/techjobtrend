import bottlenose
from bs4 import BeautifulSoup
import lxml.etree as etree  
from os.path import isfile, join
import json

ACCESS_KEY = "AKIAIJWGVA4XGB6P6OQA"
SECRET_ACCESS_KEY = "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"
ASSOCIATE_TAG = "beavis2809-20"
 
amazon = bottlenose.Amazon(ACCESS_KEY, SECRET_ACCESS_KEY, ASSOCIATE_TAG)
response1 = amazon.ItemSearch(Keywords="javascript", SearchIndex="KindleStore", ResponseGroup="Images, ItemAttributes, Offers")
soup1 = BeautifulSoup(response1,"lxml")

response2 = amazon.ItemSearch(Keywords="java", SearchIndex="KindleStore", ResponseGroup="Images, ItemAttributes, Offers")
soup2 = BeautifulSoup(response2,"lxml")

response3 = amazon.ItemSearch(Keywords="tensorflow", SearchIndex="KindleStore", ResponseGroup="Images, ItemAttributes, Offers")
soup3 = BeautifulSoup(response3,"lxml")

output_data = []


#print(soup.find_all('item')[0]('itemlinks').prettify())
#for item in soup1.find_all('item'):
index = 0
for item in soup1.find_all('item'):  
  index += 1
  output_data.append({'title': item.title.text, 'image': item.mediumimage.url.text, 'url': item.url.text})
  if index == 3:
    break

for item in soup2.find_all('item'):
  index += 1
  output_data.append({'title': item.title.text, 'image': item.mediumimage.url.text, 'url': item.url.text})
  if index == 2:
    break

for item in soup3.find_all('item'):
  index += 1
  output_data.append({'title': item.title.text, 'image': item.mediumimage.url.text, 'url': item.url.text})
  if index == 2:
    break

with open(join('result', 'amazon_data.json'), 'w') as outfile:
    json.dump(output_data, outfile)

