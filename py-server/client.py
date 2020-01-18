import socket
import json

HOST = '192.168.123.103'  # The server's hostname or IP address
PORT = 28280        # The port used by the server
# a Python object (dict):
x = {
  "name": "John",
  "age": {
      "1":30,
      "2":30,
  },
  "city": "New York",
}

# convert into JSON:
jsonToString = json.dumps(x)

# the result is a JSON string:
print(jsonToString)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for x in range(1):
        # sendData = str(x) + " Hello, world sdf " 
        sendData = jsonToString
        s.sendall(sendData.encode('utf-8'))
        data = s.recv(1024)
        pass

print('Received', repr(data))
