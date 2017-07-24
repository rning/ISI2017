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
        EchoServer(self.sock)

def outerThread(function):
    def checkWrap(*args):
        packThread = threading.Thread(target=function, args=args)
        packThread.setDaemon(True)
        packThread.start()
        return packThread
    return checkWrap

class EchoServer(asyncore.dispatcher):

    def __init__(self, sock):
        asyncore.dispatcher.__init__(self, sock=sock)

        self.seq = 0
        self.ack = 0
        self.ackCounter = 0
        self.cwnd = 1
        self.ssthresh = 0 #what initial value to set?
        self.timeoutTime = 30 #time in seconds
        self.maxwnd = 16
        self.startTime = None
        self.canWrite = True
        self.canRead = True

        logging.basicConfig(format='%(message)s', level=logging.DEBUG)

        self.packetCheck()

    def readable(self):
        return bool(self.canRead)
    def handle_read(self):
        logging.debug("handle_read reading...")

        readBuffer = self.recv(4096)
        # logging.debug(str(len(readBuffer)))
        
        for i in range(0, len(readBuffer) / 40):
            #unpack structure received from client: [seq,ack,string]
            packet = struct.unpack('LL24s', readBuffer[:40]) #size: 32 bytes
            if self.retransmit:
                logging.debug('acked ' + str(self.ack) + ' sequence ' + str(self.seq) + ' cwnd ' + str(self.cwnd))
                readbuffer = readBuffer[40:]
                break
            #if received ack is in right order increment ACK appropriately
            elif packet[1] == self.ack + 1:
                self.ack += 1
                self.seq += 1
                self.ackCounter += 1

                logging.debug('acked ' + str(self.ack) + ' sequence ' + str(self.seq) + ' cwnd ' + str(self.cwnd))
            readBuffer = readBuffer[40:]

    def writable(self):
        return bool(self.canWrite)

    def handle_write(self):
        #for loop to send cwnd# of packets
        self.retransmit = False # reset handle_read exit conditional

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
                    if self.ackCounter == self.cwnd:
                        self.ackCounter = 0
                        #if ssthresh (maxwnd size) determined, keep transmitting at cwnd
                        if self.ssthresh == self.cwnd:
                            self.canWrite = True
                            logging.debug("cwnd reached threshhold, ssthresh:" + str(self.ssthresh))
                        else:
                            self.ssthresh = self.cwnd
                            self.cwnd = self.cwnd * 2
                            self.canWrite = True
                            logging.debug("cwnd multiplied by 2, ssthresh:" + str(self.ssthresh))
                    elif self.ack > self.maxwnd:
                        self.cwnd = self.cwnd / 2
                        self.canWrite = True
                        self.retransmit = True
                        self.canRead = False
                        self.ack = self.cwnd - 1
                        self.seq = self.cwnd
                        logging.debug("exceeded maxwnd, ack = 0 -> retransmit")
                else:
                    #if function not exited by now (meaning all packets not acked), retransmit
                    #below code retransmits at half cwnd (alternative would retransmit at cwnd=1)
                    self.cwnd = self.cwnd / 2
                    if self.cwnd < 1: cwnd = 1
                    self.canWrite = True
                    logging.debug("timeout -> retransmit")

                    self.ackCounter = 0

            time.sleep(.002)

if __name__ == '__main__':
    try:
        add = str(input("Enter IP address of server in single quotes:\n"))
        s = Server(add, 8080)
    except:
        print "Your address was typed incorrectly or the port is in timeout. Try again."
    asyncore.loop(0)
