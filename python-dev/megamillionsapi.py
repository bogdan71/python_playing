import requests
import xml.etree.ElementTree as ET

response = requests.get('https://www.megamillions.com/cmspages/utilservice.asmx/GetDrawingPagingData?pageNumber=1&pageSize=1500&startDate=2010-01-01T14:00:00&endDate=2020-09-20T00:00:00')
#print(response.status_code)
print(response.content)

root = ET.fromstring(response.content)
#base = str(root)[2:-1]
#print(root)

#for child in root.findall(''):
    #print(child)

#jsondata = ''.join()
