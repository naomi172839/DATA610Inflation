import requests
import datetime
import re

endpoint = 'https://www.statbureau.org/calculate-inflation-value-json'
print()

print('case')
for year in range(1990, 2017):
    print('when ( Year_ = ' + str(year) + ' ) then')
    print('case')
    for month in range(1,13):
        query = {'country': 'united-states',
                 'start': datetime.datetime(2021, 9, 1),
                 'end': datetime.datetime(year, month, 1), 'amount': 1.00,
                 }
        response = requests.get(endpoint, params=query)
        print('when ( Month_ = ' + str(month) + ' ) then')
        print('Gross * ' + re.sub('\\$', '', response.json()))
    print('else')
    print('Gross * -1')
    print('end')

print('else')
print('Gross * -1')
print('end')

