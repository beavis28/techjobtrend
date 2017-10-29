import feedparser
import json
from os.path import join

rss_data = feedparser.parse('https://www.infoworld.com/news/index.rss')

output_data = []

for e in rss_data.entries:
    date = e.published.split()
    date = ' '.join(date[:4])
    output_data.append({'title': e.title, 'link': e.link, 'published': date, 'pic': e.media_thumbnail[0]['url']})

with open(join('result', 'rss.json'), 'w') as outfile:
    json.dump(output_data, outfile)
