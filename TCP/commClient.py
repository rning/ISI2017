import logging
import random
import socket
from threading import Thread
import threading
import time


PORT=38814
BUFF=1024
FALSE=0
TXTIMEOUT=1

log = logging.getLogger(__name__)

class ClientCommService:
    
    def __init__(self, clientId):
        self.active = False
        self.clientId = clientId
        self.connected = False
        self.sock = None
    
    def initCommClient(self, address, replyHandler):
        functionName = self.initCommClient.__name__
 #       helpers.entrylog(log, functionName, level=logging.INFO)
        
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.settimeout(TXTIMEOUT)
        
        retries = 0        
        while not self.connected:
            log.info("Trying to connect to server, attempt #%d..." % (retries+1))
            try:
                self.sock.connect((address, PORT))
                self.connected = True
                log.info("Connected to server")
            except socket.error as e:
                retries += 1
                log.info("Socket timed out, exception: %s" % repr(e))
                time.sleep(0.1 + (random.random()*0.3))

        data = {'src': self.clientId}
        self.sock.send(str(data))
        
        self.active = True
        thread = Thread(name="ClientHandler for " + self.clientId, target=self.ClientHandler, args=(replyHandler,))

	#setting to daemon so all the clients die when the main thread is dead 
        thread.daemon = True		
        thread.start()
        
  #      helpers.exitlog(log, functionName, level=logging.INFO)
        return thread
    
    def ClientHandler(self, replyHandler):
        
        t = threading.currentThread()
        log.info("Running %s"  % t.name)
        
        while self.active:
            #blocks on recv, but may timeout
            try:
                rxdata = self.sock.recv(BUFF)
                log.debug("Data Received: %s" %(repr(rxdata)))
            except socket.timeout:
                continue

            try:
                data = rxdata.strip()
            except:
                log.info("ClientHandler could not parse JSON string: %s" % repr(rxdata))
                continue
            print t 
            log.debug('Client RX jdata: %s'  %(repr(data)))
	    
	    if data == '':
		print "server disconnected"
		self.active = False
	    else: 
            	replyHandler(data)

        #cleanup
        self.sock.close()
        log.info("Leaving %s" % threading.currentThread().name)
    
    def sendData(self, data):

	tmp = eval(data)
        tmp['src'] = self.clientId
	data = str(tmp)

        log.debug('Sending data %s' %(data))
        self.sock.send(data)
                
    def stop(self):
        self.active = False

def echoHello(message):
    print "message received"


if __name__ == "__main__":

    #arguments/options get clientId
    import sys,getopt
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'i:')
    except getopt.GetoptError as err:
        print (str(err))
        print ("Arguments missing or invalid, indicate client id")
        sys.exit(2)
    

    clientId = ''

    for opt, arg in opts:
        if opt == '-i':
            clientId = arg


    

    client = ClientCommService(clientId)
    client.initCommClient('localhost',echoHello)
    dic = {'src' : clientId, 'message' : 'success'}

    client.sendData(str(dic))

    #  Example code snippet: sending multiple messages from the same client
    i = 0 
    while i < 10:
	dic = {'src' : client.clientId, 'message': i}
	client.sendData(str(dic))
	#sleep to avoid message concatination on the server
	time.sleep(2); 
	i = i + 1





    tmp = raw_input("press enter to kill client\n")

    
    client.stop()
