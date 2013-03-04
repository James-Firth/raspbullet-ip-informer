import socket
import sys
import pushbullet
from pushbullet import PushBullet


#Make sure to put your api key here to work!
apiKey = "YOUR_API_KEY_HERE"

#create pushbullet obj and get list of devices
pb = PushBullet(apiKey)
devices = pb.getDevices()
IP = sys.argv[1]

#push IP to device!
pb.Note(devices[0]["id"], "IP Address", IP)
