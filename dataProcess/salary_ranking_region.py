from os.path import isfile, join
import json
import arrow
from collections import Counter

import re

import currencylayer
exchange_rate = currencylayer.Client(access_key='1e38b05a57427f8a67dafa2c48b941e7')
#response = exchange_rate.currencies()
response = exchange_rate.live_rates(base_currency='USD')

output_data = []
location_list = []

latest_file_name = "jobs" + arrow.now().format('YYYY-MM-27') + ".json"

def convert_money_string_to_int(money):
    test = money.strip().upper()
    test = test.replace('K', '000')
    test = re.sub('[!@#$]', '', test)

    return float(test)

def average_money(money_range):
    split_part = money_range.index('-')
    first_part = convert_money_string_to_int(money_range[:split_part])
    second_part = convert_money_string_to_int(money_range[split_part:])
    return (first_part + second_part) / 2


with open(join('processed', latest_file_name), 'r') as f:
    original_data = json.load(f)

    for x in original_data:
        if not x['salary']:
            continue
        if not location_list:
            avgMoney = average_money(x['salary'])
            location_list.append({'location': x['location'], 'salary': avgMoney})
        else:
            bfind = False
            for y in location_list:

                if y['location'] == x['location']:
                    bfind = True
                    y['salary'].extend(x['salary'])

            if bfind == False:
                location_list.append({'location': x['location'], 'salary': x['salary']})

for l in location_list:
    m = dict(Counter(l['tags']))
    n = sorted(m.items(), key=lambda x: (-x[1], x[0]))
    o = n[:5]
    p = l['location'].replace("- \r\n", "")
    output_data.append({p: o})


with open(join('result', 'region_data.json'), 'w') as outfile:
    json.dump(output_data, outfile)