import socket
import threading
import time
import select
import sys

SYSTEM_HOST_ADDRESS = "localhost"
SYSTEM_SERVER_PORT = 5988

      
def streamServer(obj):
    thread = obj.thread
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setblocking(0)
    server_sock.bind( (SYSTEM_HOST_ADDRESS, SYSTEM_SERVER_PORT) )
    server_sock.listen(5)
    inputs = [ server_sock ]
    outputs = [ ]
    events = [ ]
    clients = {}
    print('starting up on {}:{}. Wait for connection...\n'.format(SYSTEM_HOST_ADDRESS, SYSTEM_SERVER_PORT) )
    while ( not thread.stop_event.is_set() ):
        if inputs:
            timeout = 1
            infds, outfds, errfds = select.select(inputs, outputs , events, timeout)
            if len(infds) != 0: # Handle inputs
                for s in infds:
                    # new connection
                    if s is server_sock:
                        connection, client_address = s.accept()
                        print('new connection from {}'.format(client_address) )
                        connection.setblocking(0)
                        # add the new client socket for monitoring
                        inputs.append(connection)
                    else: # client's message
                        data = s.recv(1024)
                        if data:
                            # A readable client socket has data
                            print('received {} from {}'.format(data, s.getpeername()) )
                            # Add output channel for response
                            if s not in outputs:
                                outputs.append(s)
                        else: # clien's disconnection
                            print(sys.stderr, 'closing', client_address, 'after reading no data' )
                            # Stop listening for input on the connection
                            if s in outputs:
                                outputs.remove(s)
                            inputs.remove(s)
                            s.close()
            elif len(outfds) != 0:
                print("out")
            elif len(events) != 0:
                print("events")
            else: # timeout
                #print("timeout")
                timeout = 1
        # no inputs 
    #
    print('{}: Signalled quit\n'.format("streamServer") )

def sendMesg():

    return


class iot_mesgServer():
    'IOT message controller'
    dbg = 0
    def __init__(self, dbg=0):
        self.dbg = dbg
        self.thread = threading.Thread(target=streamServer, args=(self, ))
    def start(self):
        self.thread.stop_event = threading.Event()
        self.thread.start()
        print("msgServer is started\n") 
        return
    def stop(self):
        self.thread.stop_event.set()
        self.thread.join()
        print("msgServer is stopped\n") 
    def stopped(self):
        self.thread.stop_event.is_set()
    

class iot_mesgClient():
    'IOT message controller'
    dbg = 0
    def __init__(self, dbg=0):
        self.dbg = dbg
    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        try:
            s.connect( (SYSTEM_HOST_ADDRESS, SYSTEM_SERVER_PORT) )
        except socket.timeout:
            s.close()
            s = None
            raise NameError("Server is not ready!")
        finally:
            self.s = s
        return
    
    



