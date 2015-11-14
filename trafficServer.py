import SocketServer
from trafficcalc import byteLoop

class TrafficStreamHandler(SocketServer.StreamRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    
    def handle(self):
        client = self.client_address[0]
        
        print "Verbindung von: {} angenommen.".format(client)
        
        try:
            byteLoop(self.wfile, 1.0)
        except:
            pass
        finally:
            print "Verbindung geschlossen: {}".format(client)
            self.request.close()

        
if __name__ == "__main__":
    HOST, PORT = "", 9999

    # Create the server, binding to localhost on port 9999
    #since we do not allow daemon_threads only one conneciton will be handled at a time
    server = SocketServer.TCPServer((HOST, PORT), TrafficStreamHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
