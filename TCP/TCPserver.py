import asyncore, socket, struct, time, threading, logging
#from ParameterParser import *

class Server(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((host, port))
        self.listen(5)
        print "Server: Waiting for connection..."

    def handle_close(self):
        print "Server: Closed"
        self.close()

    def handle_accept(self):
        self.sock, self.address = self.accept()
        print "Server: Connection by ", self.address
        self.sock.setblocking(0)
        eServ1 = EchoServer(self.sock)
        eServ1PH = eServ1.packetCheck() # call packetcheck to start the thread
        # eServ1R = eServ1.handle_read()

def outerThread(function):
    def checkWrap(*args):
        packThread = threading.Thread(target=function, args=args)
        packThread.setDaemon(True)
        packThread.start()
        return packThread
    return checkWrap

def innerReadThreadHandler(function):
    def iRTHWrapper(*args):
        rThread = threading.Thread(target=function, args=args)
        rThread.setDaemon(True)
        rThread.start()
        return rThread
    return iRTHWrapper # these returns aren't really needed, but just incase we need to reference the thread

class EchoServer(asyncore.dispatcher):

    def __init__(self, sock):
        asyncore.dispatcher.__init__(self, sock=sock)

        self.seq = 0
        self.ack = 0
        self.iSeq = 0
        self.cwnd = 1
        self.ssthresh = 0 #what initial value to set?
        self.timeoutTime = 5 #time in seconds
        self.maxwnd = 8
        self.startTime = None
        self.canWrite = True
        self.wcount = 0
        self.canRead = False
        self.rcount = 0
        self.canContinue = True
        logging.basicConfig(format='%(message)s', level=logging.DEBUG)
        
    # @innerReadThreadHandler
    def handle_read(self):
        # while True:
        logging.debug("handle_read reading...")
        self.canContinue = False


        #unpack structure received from client: [seq,ack,string]
        packet = struct.unpack('LL24s', self.recv(4096)) #size: 32 bytes
        
        #if received ack is in right order increment ACK appropriately
        # while not self.canContinue: 
        if packet[1] == self.ack + 1:
            self.ack += 1
            self.seq += 1#

        #debug
        logging.debug('acked ' + str(self.ack) + ' sequence ' + str(self.seq) + ' cwnd ' + str(self.cwnd))
        time.sleep(.002)
    # time.sleep(.002)
        self.canWrite = True
        self.canRead = False

    def writable(self):
        self.wcount += 1
        if self.wcount <= 50:
            logging.debug("writeable: " + str(self.canWrite))
        return bool(self.canWrite)

    def readable(self):
        self.rcount += 1
        if self.wcount <= 50:
            print "readable: ", self.canRead
        return bool(self.canRead)

    def handle_write(self):
        #print "handle_write sending..."

        #for loop to send cwnd# of packets
        for i in range(1, (self.cwnd + 1)):
            #pack structure and send to client: [seq,ack,string]
            self.send(struct.pack('LL24s', self.seq + i, self.ack, 'data'))

            #debug
            logging.debug('sent packet with seq# ' + str(self.seq + i) + ' ack# ' + str(self.ack)) 

        self.canWrite = False
        self.canRead = True
        self.startTime = time.time()

    @outerThread
    def packetCheck(self):
        while True: 
            if self.startTime is None:
                pass
            else:
                if time.time() - self.startTime < self.timeoutTime:
                    #exit timeout if all packets acked
                    if self.ack == self.seq + self.cwnd: # These ifs don't run if you use + self.cwnd. Perhaps these can never be fulfilled?
                        #if ssthresh (maxwnd size) determined, keep transmitting at cwnd
                        if self.ssthresh == self.cwnd:
                            self.canContinue = True
                        else:
                            self.ssthresh = self.cwnd
                            self.cwnd = self.cwnd * 2
                            self.canContinue = True
                            logging.debug("cwnd multiplied by 2")
                else:
                    #if function not exited by now (meaning all packets not acked), retransmit
                    #below code retransmits at half cwnd (alternative would retransmit at cwnd=1)
                    self.cwnd = self.cwnd / 2
                    if self.cwnd < 1: cwnd = 1
            time.sleep(.002)


 

if __name__ == '__main__':
    try:
        add = str(input("Enter IP address of server in single quotes:\n"))
        s = Server(add, 8080)
    except:
        print "Your address was typed incorrectly or the port is in timeout. Try again."
    asyncore.loop(20) #(0)
