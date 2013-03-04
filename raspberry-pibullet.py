import socket
import sys
import pushbullet
from pushbullet import PushBullet
from socket import socket, SOCK_DGRAM, AF_INET 

#getting IP address
s = socket(AF_INET, SOCK_DGRAM) 
s.connect(('google.com', 0))#using Google since it's pretty well always reachable
IP = s.getsockname()[0] #grab IP portion

#Make sure to put your api key here to work!
apiKey = "YOUR_API_KEY_HERE"

#create pushbullet obj and get list of devices
pb = PushBullet(apiKey)
devices = pb.getDevices()

#push IP to device!
pb.pushNote(devices[0]["id"], "IP Address", IP)
