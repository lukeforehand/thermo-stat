#!/usr/bin/python
import sys
import socket
import json
import urllib2

graphite_host = 'graphite.colo.networkedinsights.com'
graphite_port = 2013
json_source = 'https://www.lacrossealerts.com/v1/observations/9509?format=json&from=-1days'
device='luke.porch'
auth_cookie = sys.argv[1]

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', auth_cookie))
data = json.load(opener.open(json_source))
sock = socket.socket()
sock.connect((graphite_host, graphite_port))
message = ""
for item in data.get('response').get('obs'):
  message = message + device + '.probe.temp ' + `item.get('values').get('temp')` + ' ' + `item.get('timeStamp')` + '\n'
  message = message + device + '.ambient.temp ' + `item.get('values').get('temp2')` + ' ' + `item.get('timeStamp')` + '\n'
  message = message + device + '.humidity.pct ' + `item.get('values').get('rh')` + ' ' + `item.get('timeStamp')` + '\n'
print message
sock.sendall(message)
sock.close()
