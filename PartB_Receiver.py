import socket
import json

PORT = 9999

receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
receiver.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
receiver.bind(('',PORT))

while True:
    data, addr = receiver.recvfrom(1024)
    response = json.loads(data.decode())
    
    print('Server Address: {0} Server Time: {1}'.format(addr, response['serverTime']))
    print('Disaster Information Broadcast Information')
    print('Date of disaster occurrence: {}'.format(response['date']))
    print('Time of disaster occurrence: {}'.format(response['time']))
    print('Type of disaster: {}'.format(response['type']))
    print('Location of disaster occurrence: {}'.format(response['location']))
    print('Desciption of disaster: {}'.format(response['description']))
    print('')