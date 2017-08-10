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
      'breweryCount': row[4],
      'breweriesPerCapita': row[5]
    }
    data.append(state_data)


with open('data/breweries_per_capita.json', 'w') as fp:
  json.dump(data, fp)

