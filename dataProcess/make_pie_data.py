from os.path import isfile, join
import json

data = {}
data['key'] = 'value'
json_data = json.dumps(data)
values = []
labels = []
output_data =[]

with open(join('result', 'data.json'), 'r') as f:

    original_data = json.load(f)
    process_data = original_data[-1]['tags']

    index = 0
    for x in process_data:
        values.append(x['perc'])
        labels.append(x['tag'])
        index += 1
        if index > 50:
            break

    output_data = {"values": values, "labels": labels, "type": "pie"}

with open(join('result', 'pie_data.json'), 'w') as outfile:
    json.dump(output_data, outfile)