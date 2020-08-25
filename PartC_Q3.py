import http.client
import csv
import json

HOST = 'localhost'
PORT = 8888

print('Connecting to Host: {0}, Port: {1}'.format(HOST,PORT))
conn = http.client.HTTPConnection(HOST,PORT)

with open('UpdateStations.csv') as file:
    stations = csv.DictReader(file)
    for station in stations:
        station = dict(station)
        
        print('Sending HTTP Put Request...')
        conn.request('PUT', '/api/stations/' + station['id'], json.dumps(station), {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        })
    
        print('Receiving HTTP Put Response...')
        resp = conn.getresponse()
        if resp.status == 201:
            result = json.loads(resp.read())
            print(result)
        else:
            print('Error: {}'.format(resp.status))
