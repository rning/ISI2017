import asyncore, socket, struct, time
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

class EchoServer(asyncore.dispatcher):

    def __init__(self, sock):
        asyncore.dispatcher.__init__(self, sock=sock)

        self.seq = 0
        self.ack = 0
        self.cwnd = 1
        self.ssthresh = 0 #what initial value to set?
        self.timeoutTime = 5 #time in seconds
        self.maxwnd = 8
        self.startTime = None
        self.canWrite = True
        self.wcount = 0
        self.canRead = False
        self.rcount = 0

    def handle_read(self):
        print "handle_read reading..."

        #unpack structure received from client: [seq,ack,string]
        packet = struct.unpack('LL24s', self.recv(4096)) #size: 32 bytes
        
        #if received ack is in right order increment ACK appropriately
        if packet[1] == self.ack + 1:
            self.ack += 1
            self.seq += 1#

            #debug
            print 'acked', self.ack, 'sequence', self.seq, 'cwnd', self.cwnd
        self.canWrite = True
        self.canRead = False
    def writable(self):
        if not self.canRead:
            if self.startTime is None:
                pass
            else:
                if time.time() - self.startTime < self.timeoutTime:
                    #exit timeout loop if all packets acked
                    if self.ack == self.seq + self.cwnd:
                        #if ssthresh (maxwnd size) determined, keep transmitting at cwnd
                        if self.ssthresh == self.cwnd:
                            self.canWrite = True
                        else:
                            self.ssthresh = self.cwnd
                            self.cwnd = self.cwnd * 2
                            self.canWrite = True
                else:
                    #if function not exited by now (meaning all packets not acked), retransmit
                    #below code retransmits at half cwnd (alternative would retransmit at cwnd=1)
                    self.cwnd = self.cwnd / 2
                    if self.cwnd < 1: cwnd = 1
                    self.canWrite = True
            self.wcount += 1
            if self.wcount <= 50:
                print "writeable: ", self.canWrite
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
            print 'sent packet with seq#' , self.seq + i, 'ack#', self.ack 

        self.canWrite = False
        self.canRead = True
        self.startTime = time.time()
    
    def packetController(self):
        print "packetController called"


 

if __name__ == '__main__':

    add = str(input("Enter IP address of server in single quotes:\n"))
    s = Server(add, 8080)

    asyncore.loop(1) #(0)
