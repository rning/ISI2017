
import logging
import socket
from threading import Thread
import threading

#from magi.util import helpers


PORT=38814
BUFF=1024
FALSE=0
TXTIMEOUT=1


log = logging.getLogger(__name__)

class ServerCommService:
    
    def __init__(self):
        self.active = False
        self.transportMap = dict()
        self.threadMap = dict()
        self.sock = None
    
    def initCommServer(self, replyHandler):
        functionName = self.initCommServer.__name__
 #       helpers.entrylog(log, functionName, level=logging.INFO)
        
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#         sock = socket.socket(socket.AF_INET, # Internet
#                              socket.SOCK_DGRAM) # UDP
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.settimeout(TXTIMEOUT)
        self.sock.bind(('0.0.0.0', PORT))
        self.sock.listen(5)
        
        self.active = True
        thread = Thread(target=self.commServerThread,args=(replyHandler,))
        thread.start()
        
  #      helpers.exitlog(log, functionName, level=logging.INFO)
        return thread
    
    #Blocking, never returns
    def commServerThread(self, replyHandler):
        
        log.info("Running commServerThread on %s" % threading.currentThread().name)
        
        while self.active:
            try:
                clientsock, addr = self.sock.accept()
                rxdata = clientsock.recv(BUFF)
            except socket.timeout:
                continue

            try:
                data = eval(rxdata.strip())
            except:
                log.info("Exception in commServerThread while trying to parse JSON %s" % repr(rxdata))
                continue
            
            log.info("New Connection: %s" %(data))

            clientId = data['src']
            nthread = Thread(name="ServerHandler for " + clientId, target=self.ServerHandler, args=(clientId, clientsock, replyHandler))
            self.threadMap[clientId] = nthread
            self.transportMap[clientId] = clientsock

	    #setting to daemon so all the client handlers die when the main thread is dead 
	    nthread.daemon = True		

            nthread.start()
            
            log.info('Client %s connected.' %(clientId))
            
        log.info("Leaving commServerThread %s" % threading.currentThread().name)
        self.sock.close()
        
    #One thread is run per client on the servers's side
    def ServerHandler(self, clientId, clientsock, replyHandler):
        t = threading.currentThread()

        clientsock.settimeout(TXTIMEOUT);
        log.info("Running %s" % t.name)
        
        while self.active:
            try:
                rxdata = clientsock.recv(BUFF)
                log.debug("Data Received: %s" %(repr(rxdata)))
            except socket.timeout:
                continue

            try:
                data = rxdata.strip()
            except :
                log.info("Exception in ServerHandler while trying to parse JSON string: %s" % repr(rxdata))
                continue

            log.debug('ServerHandler RX data: %s' % repr(data))
	    if data == '':
	     	print "client ", clientId," disconnected"
		break
	    else:            
		replyHandler(data)

        #Cleanup
        clientsock.close()
        log.info("Leaving %s" % t.name)
    
    def sendData(self, clientId, data):
        data['dst'] = clientId
       # data = json.dumps(data)
        
        if clientId not in self.transportMap:
            log.error("Client %s not registered" %(clientId))
            raise Exception, "Client %s not registered" %(clientId)
            
        clientsock = self.transportMap[clientId]
        
        log.debug('Sending data %s' %(data))
        clientsock.send(str(data))
                    
    def stop(self):
        self.active = False

#should not be a global. for testing
server = ServerCommService()
def echohandler(message):
    print "got it"
    print message
    print "\n"

    #expects exacly one dictionary
    #dic = eval(message)
    #server.sendData(dic['src'],dic)


if __name__ == "__main__":

    server.initCommServer(echohandler)

    tmp = raw_input("press enter to kill server\n")

    server.stop()



