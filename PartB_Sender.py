import socket
import json
import time
from datetime import datetime

PORT = 9999

sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

dDate = input("Enter the date of disaster occurrence: ")
dTime = input("Enter the time of disaster occurrence: ")
dType = input("Enter the type of disaster: ")
dLoc = input("Enter the location of disaster occurrence: ")
dDesc = input("Enter the description of disaster: ")

while True:
    serverTime = str(datetime.now())
    
    dict = {
            'serverTime': serverTime,
            'date':dDate,
            'time':dTime,
            'type':dType,
            'location':dLoc,
            'description':dDesc
            }
    
    response = json.dumps(dict)
    
    sender.sendto(response.encode(),('<broadcast>', PORT))
    print('Broadcast data to UDP Port {}'.format(PORT))
    
    time.sleep(1)