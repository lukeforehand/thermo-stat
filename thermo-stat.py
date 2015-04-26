#!/usr/bin/python
import sys
import socket
import json
import urllib2

graphite_host = 'graphite.colo.networkedinsights.com'
graphite_port = 2013
json_source = 'https://www.lacrossealerts.com/v1/observations/9509?format=json&from=-1days'
auth_cookie = sys.argv[1]

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', auth_cookie))
data = json.load(opener.open(json_source))
sock = socket.socket()
sock.connect((graphite_host, graphite_port))
for item in data.get('response').get('obs'):
  message = 'luke.porch.probe ' + `item.get('values').get('temp')` + ' ' + `item.get('timeStamp')` + '\n'
  print message
  sock.sendall(message)
  message = 'luke.porch.ambient ' + `item.get('values').get('temp2')` + ' ' + `item.get('timeStamp')` + '\n'
  print message
  sock.sendall(message)
  message = 'luke.porch.humidity ' + `item.get('values').get('rh')` + ' ' + `item.get('timeStamp')` + '\n'
  print message
  sock.sendall(message)
sock.close()
