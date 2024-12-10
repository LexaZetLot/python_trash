import sys, http.client
showlines = 6
try:
    servername, filename = sys.argv[1:]
except:
    servername, filename = 'learning-python.com', '/index.html'

print(servername, filename)
server = http.client.HTTPConnection(servername)
server.putrequest('GET', filename)
server.putheader('Accept', 'text/html')
server.endheaders()

reply = server.getresponse()
if reply.status != 200:
    print('Error sending request', reply.status, reply.reason)
else:
    data = reply.readlines()
    reply.close()
    for line in data[:showlines]:
        print(line)