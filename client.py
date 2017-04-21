#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect(("103.72.177.22", port))
print (s.recv(1024))
s.close                     # Close the socket when done