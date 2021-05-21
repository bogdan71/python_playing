import requests
import xml.etree.ElementTree as ET
import json

allNumsList = []

for year in range(2010, 2022, 1):
    print(year)
    response = requests.get('https://www.powerball.com/api/v1/numbers/powerball?_format=json&min='+str(year)+'-01-01%2000:00:00&max='+str(year)+'-12-31%2023:59:59')
    root = json.loads(response.text)
    for key in root:
        #print(key['field_winning_numbers'])
        allNumsList.append(key['field_winning_numbers'])
#'4,18,27,34,50,22'
for elem in allNumsList:
    if ',1' in elem:
        print(elem)


#print(allNumsList)


#response = requests.get('https://www.powerball.com/api/v1/numbers/powerball?_format=json&min=2018-01-01%2000:00:00&max=2018-12-31%2023:59:59')

#print(response.status_code)
#print(response.content)

#root = json.loads(response.text)
#print(root)


#for key in root:
#    print(key['field_winning_numbers'])
#    print(key['field_draw_date'])