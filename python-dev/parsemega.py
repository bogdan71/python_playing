import json

with open('megadata.json') as json_file:
    data = json.load(json_file)
    #cnt = 0
    for p in data['DrawingData']:
        #cnt += (str(p['MBall']).count('14'))
        print(p['PlayDate'],'\t', p['N1'], '\t',p['N2'],'\t',p['N3'], '\t',p['N4'],'\t',p['N5'], '\t',p['MBall'])
    #print(cnt)
