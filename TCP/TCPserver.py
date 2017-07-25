import asyncore, socket, struct, time, threading, logging, sys
from ParameterParser import parameter

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
        pStartTime = time.time()
        EchoServer(self.sock)

def outerThread(function):
    def checkWrap(*args):
        packThread = threading.Thread(target=function, args=args)
        packThread.setDaemon(True)
        packThread.start()
        return packThread
    return checkWrap

def logThreadHandler(function):
    def handleWrapper(*args):
        logThread = threading.Thread(target=function, args=args)
        logThread.setDaemon(True)
        logThread.start()
        return logThread
    return handleWrapper

class EchoServer(asyncore.dispatcher):

    def __init__(self, sock):
        asyncore.dispatcher.__init__(self, sock=sock)

        self.seq = 0
        self.ack = 0
        self.ackCounter = 0
        self.cwnd = 1
        self.ssthresh = 0 #what initial value to set?
        self.timeoutTime = 4 #time in seconds
        self.maxwnd = 16
        self.startTime = None
        self.canWrite = True
        self.canRead = True
        self.packetLength = 32

        logging.basicConfig(format='%(message)s', filename='XYlog.txt', filemode='w', level=logging.DEBUG)
        self.initParams()
        self.logThread()
        self.packetCheck()
        gThreadDelay = self.threadDelay

    def initParams(self):
        self.maxwnd = int(parameter("maxwnd"))
        # logging.debug("MAXWND IS: " + str(self.maxwnd))
        self.timeoutTime = int(parameter("timeoutTime"))
        self.programTotalMaxTime = int(parameter("programTotalMaxTime")) 
        self.ssthreshEnabled = bool(parameter("ssthreshEnabled"))
        self.threadDelay = float(parameter("Delay"))

    def readable(self):
        return bool(self.canRead)

    def handle_read(self):
        # logging.debug("handle_read reading...")
        self.isSending = False

        readBuffer = self.recv(4096)
        # logging.debug(str(len(readBuffer)))
        
        for i in range(0, len(readBuffer) / self.packetLength):
            #unpack structure received from client: [seq,ack,string]
            packet = struct.unpack('LL24s', readBuffer[:self.packetLength]) #size: 32 bytes
            if self.retransmit:
                # logging.debug('acked ' + str(self.ack) + ' sequence ' + str(self.seq) + ' cwnd ' + str(self.cwnd))
                readbuffer = readBuffer[self.packetLength:]
                break
            #if received ack is in right order increment ACK appropriately
            elif packet[1] == self.ack + 1:
                self.ack += 1
                self.seq += 1
                self.ackCounter += 1

                # logging.debug('acked ' + str(self.ack) + ' sequence ' + str(self.seq) + ' cwnd ' + str(self.cwnd))
            readBuffer = readBuffer[self.packetLength:]

    def writable(self):
        return bool(self.canWrite)

    def handle_write(self):
        #for loop to send cwnd# of packets
        self.retransmit = False # reset handle_read exit conditional
        afterTransmitCounter = 0
        
        self.isSending = True
        for i in range(1, (self.cwnd + 1)):
            #pack structure and send to client: [seq,ack,string]
            self.send(struct.pack('LL24s', self.seq + i, self.ack, 'data'))
            #debug
            # logging.debug('sent packet with seq# ' + str(self.seq + i) + ' ack# ' + str(self.ack))

        self.canWrite = False
        self.canRead = True
        self.startTime = time.time()

    @outerThread
    def packetCheck(self):
        while True: 
            if self.startTime is None:
                pass
            elif time.time() - pStartTime >= self.programTotalMaxTime:
                # logging.warning('Program reached set max time, exiting')
                sys.exit()
            else:
                if time.time() - self.startTime < self.timeoutTime:
                    #exit timeout if all packets acked
                    if self.ackCounter == self.maxwnd and not self.isSending:
                        self.ackSaved = self.ack + 1
                        self.seqSaved = self.seq + 1
                        if self.ackCounter > self.maxwnd:
                            self.canWrite = True
                            self.retransmit = True
                            self.canRead = False
                            self.cwnd = self.cwnd / 2
                            self.ack = self.ackSaved
                            self.seq = self.seqSaved
                            # logging.debug("exceeded wnd, -> retransmit")
                    elif self.ackCounter == self.cwnd:
                        self.ackCounter = 0
                        #if ssthresh (maxwnd size) determined, keep transmitting at cwnd
                        if self.ssthresh == self.cwnd and self.ssthreshEnabled:
                            self.canWrite = True
                            # logging.debug("cwnd reached threshhold, ssthresh: " + str(self.ssthresh))
                        elif self.ssthresh is not self.cwnd:
                            self.ssthresh = self.cwnd
                            self.cwnd = self.cwnd * 2
                            self.canWrite = True
                            # logging.debug("cwnd multiplied by 2, ssthresh:" + str(self.ssthresh))
                else:
                    #if function not exited by now (meaning all packets not acked), retransmit
                    #below code retransmits at half cwnd (alternative would retransmit at cwnd=1)
                    self.cwnd = self.cwnd / 2
                    if self.cwnd < 1: cwnd = 1
                    self.canWrite = True
                    # logging.debug("timeout -> retransmit")

                    self.ackCounter = 0
            time.sleep(self.threadDelay)

    @logThreadHandler
    def logThread(self):
        while(True):
            logging.info('%s %s', self.cwnd, time.time() - pStartTime)
            time.sleep(self.threadDelay)

if __name__ == '__main__':
    pStartTime = time.time()
    gThreadDelay = float(parameter("Delay"))
    try:
        add = str(input("Enter IP address of server in single quotes:\n"))
        s = Server(add, 8080)
    except:
        print "Your address was typed incorrectly or the port is in timeout. Try again."
    asyncore.loop(gThreadDelay)
