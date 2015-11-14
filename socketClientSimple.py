import socket
import sys

from struct import unpack

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.1.1', 9999)
print 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    
    while True:
        data = sock.recv(8)
        
        if len(data)==8:
            rxRate,txRate=unpack("!II", data)
            #convert to MBit
            rxRate = float(rxRate) * 8.0 / 1e6
            txRate = float(txRate) * 8.0 / 1e6
            
            #
            print "Rx: {:.3f} MBit/s, Tx:{:.3f} MBit/s".format(rxRate, txRate)

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()