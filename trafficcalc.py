import re
import time
from struct import pack

#Quelle: http://stackoverflow.com/questions/24897608/how-to-find-network-usage-in-linux-programatically
# A regular expression which separates the interesting fields and saves them in named groups
regexp = r"""
  \s*                     # a interface line  starts with none, one or more whitespaces
  (?P<interface>\w+(-\w*)*):\s+  # the name of the interface followed by a colon and spaces
  (?P<rx_bytes>\d+)\s+    # the number of received bytes and one or more whitespaces
  (?P<rx_packets>\d+)\s+  # the number of received packets and one or more whitespaces
  (?P<rx_errors>\d+)\s+   # the number of receive errors and one or more whitespaces
  (?P<rx_drop>\d+)\s+      # the number of dropped rx packets and ...
  (?P<rx_fifo>\d+)\s+      # rx fifo
  (?P<rx_frame>\d+)\s+     # rx frame
  (?P<rx_compr>\d+)\s+     # rx compressed
  (?P<rx_multicast>\d+)\s+ # rx multicast
  (?P<tx_bytes>\d+)\s+    # the number of transmitted bytes and one or more whitespaces
  (?P<tx_packets>\d+)\s+  # the number of transmitted packets and one or more whitespaces
  (?P<tx_errors>\d+)\s+   # the number of transmit errors and one or more whitespaces
  (?P<tx_drop>\d+)\s+      # the number of dropped tx packets and ...
  (?P<tx_fifo>\d+)\s+      # tx fifo
  (?P<tx_frame>\d+)\s+     # tx frame
  (?P<tx_compr>\d+)\s+     # tx compressed
  (?P<tx_multicast>\d+)\s* # tx multicast
"""


pattern = re.compile(regexp, re.VERBOSE)


def get_bytes(interface_name):
    '''returns tuple of (rx_bytes, tx_bytes) '''
    with open('/proc/net/dev', 'r') as f:
        a = f.readline()
        while(a):
            m = pattern.search(a)
            # the regexp matched
            # look for the needed interface and return the rx_bytes and tx_bytes
            if m:
                if m.group('interface') == interface_name:
                    return (m.group('rx_bytes'),m.group('tx_bytes'))
            a = f.readline()


def byteLoopDemo(stream):
    while True:
        last_bytes = get_bytes('br-lan')
        time.sleep(1)
        now_bytes = get_bytes('br-lan')
        stream.write( "rx: %s B/s, tx %s B/s\n" % (int(now_bytes[0]) - int(last_bytes[0]), int(now_bytes[1]) - int(last_bytes[1])))
        

waitTime_S = 1.0
def byteLoop(stream, waitTime_S = 1.0):
    while True:
        last_bytes = get_bytes('br-lan')
        time.sleep(waitTime_S)
        now_bytes = get_bytes('br-lan')
        #stream.write( "rx: %s B/s, tx %s B/s\n" % (int(now_bytes[0]) - int(last_bytes[0]), int(now_bytes[1]) - int(last_bytes[1])))        
        
        txRate=int((float(now_bytes[0]) - float(last_bytes[0]) ) / waitTime_S)
        rxRate=int((float(now_bytes[1]) - float(last_bytes[1]) ) / waitTime_S)
        
        stream.write(pack("!II", rxRate,txRate))
        
        