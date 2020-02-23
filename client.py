import socket
import sys
import os, os.path

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM,0)


# if os.path.isfile("tpf_unix.sock.client"):
#     print("Yass")

os.unlink("tpf_unix_sock.client")
sock.bind("tpf_unix_sock.client")


# Connect the socket to the port where the server is listening


server_address = 'tpf_unix_sock.server'
print >>sys.stderr, 'connecting to %s' % server_address
try:
    sock.connect(server_address)
except socket.error, msg:
    print >>sys.stderr, msg
    sys.exit(1)
