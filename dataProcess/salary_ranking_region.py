# -*- coding: utf-8 -*-

from os.path import isfile, join
import json
import arrow
from collections import Counter
from forex_python.converter import CurrencyRates

import re

output_data = []
location_list = []
currency_rate = CurrencyRates()

latest_file_name = "jobs" + arrow.now().format('YYYY-MM-05') + ".json"

def hasNumbers(inputString):
    return all(char.isalpha() for char in inputString)

def convert_money_string_to_int(money, currency_mark):
    test = money.strip().upper()
    test = test.replace('K', '000')
    test = re.sub("\D", "", test)
    test = test.strip()
    test = float(test)

    if currency_mark == u'€':
       test = currency_rate.convert('EUR', 'USD', test)
    elif currency_mark == 'C':
        test = currency_rate.convert('CAD', 'USD', test)
    elif currency_mark == 'N':
        test = currency_rate.convert('NZD', 'USD', test)
    elif currency_mark == u'£':
        test = currency_rate.convert('GBP', 'USD', test)
    elif currency_mark == 'A':
        test = currency_rate.convert('AUD', 'USD', test)
    elif currency_mark == 'K':
        test = currency_rate.convert('KRW', 'USD', test)
    elif currency_mark == u'₹':
        test = currency_rate.convert('IDR', 'USD', test)
    elif currency_mark == '$':
        test = test
    elif currency_mark == 'z':
        test = currency_rate.convert('PLN', 'USD', test)
    elif currency_mark == u'₪':
        test = currency_rate.convert('ILS', 'USD', test)
    elif currency_mark == 'k':
        test = currency_rate.convert('SEK', 'USD', test)
    elif currency_mark == 'R':
        test = currency_rate.convert('MYR', 'USD', test)
    else:
        print(currency_mark)


    return test

def average_money(money_range):
    split_part = money_range.index('-')
    first_part = convert_money_string_to_int(money_range[:split_part], money_range[0])
    second_part = convert_money_string_to_int(money_range[split_part:], money_range[0])
    return (first_part + second_part) / 2

with open(join('processed', latest_file_name), 'r') as f:
    original_data = json.load(f)

    for x in original_data:
        location = ""
        if x['remote']:
            continue
        if x['location']:
            location = x['location'].replace("- \r\n", "").strip()
        else:
            continue

        if not x['salary']:
            continue
        if hasNumbers(x['salary']):
            continue
        if not location_list:
            avgMoney = average_money(x['salary'])
            location_list.append({'location': location, 'salary': avgMoney, 'tags': x['tags']})
        else:
            bfind = False
            for y in location_list:

                if y['location'] == location:
                    bfind = True
                    y['tags'].extend(x['tags'])
                    avgMoney = average_money(x['salary'])
                    avgMoney_again = (y['salary'] + avgMoney)/2
                    y['salary'] = avgMoney_again
                    break

            if bfind == False:
                avgMoney = average_money(x['salary'])
                location_list.append({'location': location, 'salary': avgMoney, 'tags': x['tags']})

for l in location_list:
    m = dict(Counter(l['tags']))
    n = sorted(m.items(), key=lambda x: (-x[1], x[0]))
    o = n[:5]
    p = l['location'].replace("- \r\n", "")
    output_data.append({'salary': l['salary'], p: o})

output_data = sorted(output_data, key=lambda k: k['salary'])


with open(join('result', 'region_salary_data.json'), 'w') as outfile:
    json.dump(output_data, outfile)