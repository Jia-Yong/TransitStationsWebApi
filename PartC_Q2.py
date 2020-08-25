import http.client
import csv
import json

HOST = 'localhost'
PORT = 8888

print('Connecting to Host: {0}, Port: {1}'.format(HOST,PORT))
conn = http.client.HTTPConnection(HOST,PORT)

print('Sending HTTP Get Request...')
conn.request('GET', '/api/stations')

print('Receiving HTTP Get Response...')
resp = conn.getresponse()
if resp.status == 200:
    stations = json.loads(resp.read())
    
    print('Saving into a CSV file...')
    with open('TransitStations.csv','w',newline='') as file:
        fields = [
                'id',
                'code',
                'name',
                'type'
                ]
        
        writer = csv.DictWriter(file,fieldnames=fields)
        writer.writeheader()
        for station in stations:
            writer.writerow(station)
            
        print('Saving process is completed.')

else:
    print('Error: {}'.format(resp.status))
    
