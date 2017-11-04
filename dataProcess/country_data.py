from os.path import isfile, join
import json
import arrow
from collections import Counter

output_data = []
location_list = []

latest_file_name = "jobs" + arrow.now().format('YYYY-MM-DD') + ".json"

with open(join('processed', latest_file_name), 'r') as f:
    original_data = json.load(f)

    for x in original_data:
        location = ""
        if x['location']:
            location = x['location'].split(",")[-1].strip()
        else:
            continue
        if not location_list:
            location_list.append({'location': location, 'tags': x['tags']})
        else:
            bfind = False
            for y in location_list:

                if y['location'] == location:
                    bfind = True
                    y['tags'].extend(x['tags'])
                    break

            if bfind == False:
                location_list.append({'location': location, 'tags': x['tags']})

for l in location_list:
    m = dict(Counter(l['tags']))
    n = sorted(m.items(), key=lambda x: (-x[1], x[0]))
    o = n[:5]
    p = l['location'].replace("- \r\n", "")
    output_data.append({p: o})


output_data = sorted(output_data)

with open(join('result', 'country_data.json'), 'w') as outfile:
    json.dump(output_data, outfile)