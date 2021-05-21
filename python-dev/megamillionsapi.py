import requests
import xml.etree.ElementTree as ET
import json

response = requests.get('https://www.megamillions.com/cmspages/utilservice.asmx/GetDrawingPagingData?pageNumber=1&pageSize=1500&startDate=2010-01-01T14:00:00&endDate=2021-01-20T00:00:00')
#print(response.status_code)
#print(response.content)

root = ET.fromstring(response.content)
justdata = root.text
jsonObj = json.loads(justdata)
allNumsList = []
for key in jsonObj:
    value = jsonObj[key]
    print(key)
    if(key == 'DrawingData'):
        for p in value:
            oneline = p['PlayDate'],p['N1'],p['N2'],p['N3'],p['N4'],p['N5'],p['MBall']
            areallist = list(oneline)
            allNumsList.append(areallist)
            #print(p['PlayDate'],'\t', p['N1'], '\t',p['N2'],'\t',p['N3'], '\t',p['N4'],'\t',p['N5'], '\t',p['MBall'])
    #else:
print(allNumsList)

#for item in allNumsList:
    #data1 = item[1:]
    #print(data1)
    #for item2 in allNumsList:
        #data2 = item2[1:]
        #print(data2)
        #print(data1.intersection(data2))

#for p in root.text:
        #print(p['PlayDate'],'\t', p['N1'], '\t',p['N2'],'\t',p['N3'], '\t',p['N4'],'\t',p['N5'], '\t',p['MBall'])

#base = str(root)[2:-1]
#print(root)

#for child in root.findall(''):
#    print(child)

#jsondata = ''.join()


#    print(p['PlayDate'],'\t', p['N1'], '\t',p['N2'],'\t',p['N3'], '\t',p['N4'],'\t',p['N5'], '\t',p['MBall'])
#dt = root.find('PlayDate')
#dt[10]
#for child in dt:
    #print(child[0])
