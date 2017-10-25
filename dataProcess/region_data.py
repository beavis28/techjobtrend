from os.path import isfile, join
import json
import arrow
from collections import Counter


output_data = []
location_list = []
job_count = 0

latest_file_name = "jobs" + arrow.now().format('YYYY-MM-22') + ".json"

with open(join('processed', latest_file_name), 'r') as f:
    original_data = json.load(f)

    for x in original_data:
        job_count += 1
        if not location_list:
            location_list.append({'location': x['location'], 'tags': x['tags']})
        else:
            bfind = False
            for y in location_list:

                if y['location'] == x['location']:
                    bfind = True
                    y['tags'].extend(x['tags'])

            if bfind == False:
                location_list.append({'location': x['location'], 'tags': x['tags']})

for l in location_list:
    m = dict(Counter(l['tags']))
    n = sorted(m.items(), key=lambda x: (-x[1], x[0]))
    output_data.append({l['location']: n})


with open(join('result', 'region_data.json'), 'w') as outfile:
    json.dump(output_data, outfile)