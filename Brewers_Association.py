# extraction of data from https://www.brewersassociation.org/category/insights/

import xlrd
import json

data = xlrd.open_workbook('data/Brewers_Association_Brewery_Data.xls')
sheet = data.sheet_by_name('Capita per Brewery')

data = []
for i in xrange(sheet.nrows):
  row = sheet.row_values(i)
  if i > 0 and i < 52:
    state_data = {
      'state': row[0],
      'brewery_count': row[4],
      'capita_per_brewery': row[5]
    }
    data.append(state_data)

data.sort(key=lambda x: x['state'])

with open('data/brewery_count_by_state.json', 'w') as fp:
  json.dump(data, fp)

