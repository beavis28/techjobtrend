from os.path import isfile, join
import json
import arrow


data = {}
data['key'] = 'value'
json_data = json.dumps(data)
values = []
labels = []
output_data = []

latest_file_name = "tags-jobs" + arrow.now().format('YYYY-MM-DD') + ".json"

with open(join('result', 'tags', latest_file_name), 'r') as f:

    original_data = json.load(f)

    index = 0
    total = 0
    for x in original_data:
        values.append(int(x[1]))
        total += int(x[1])
        labels.append(x[0])
        index += 1
        if index > 50:
            total += int(x[1])
            break

    values.append(int(total) - sum(values))
    labels.append('others')
    output_data.append({"values": values, "labels": labels, "type": "pie"})

with open(join('result', 'pie_data.json'), 'w') as outfile:
    json.dump(output_data, outfile)