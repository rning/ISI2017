import asyncore, socket, struct
#from ParameterParser import *

class Server(asyncore.dispatcher):

    def __init__(self, host, port): #don't need message
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
        self.sock.send(struct.pack('L60s', 0, '')) #sends empty packet to trigger Client handle_connect
        EchoServer(self.sock)

class EchoServer(asyncore.dispatcher):

    def __init__(self, sock):
        asyncore.dispatcher.__init__(self, sock=sock)
        self.packReq = 0
        self.ackSeq = 0
        self.canWrite = True
        self.outBuffer = "testbufferwhodis" #

        self.cwnd = 1
        self.packetController()

    def readable(self):
        print "Readable -> True"
        return True

    def handle_read(self):
        print "handle_read reading..."

        #unpack structure received from client: [ack seq]
        recPack = struct.unpack('LL', self.recv(4096)) #size: 8 bytes
        
        #if pack sequence and ack sequence is 0 (empty), set data as packReq
        #else if pack sequence is 0(empty) and ack sequence >= 1, increment ACK appropriately
        if recPack[0] == (self.ackSeq + 1):
            self.ackSeq += 1
        elif recPack[0] == 0:
            self.packReq = recPack[1]

        #need timeout somewhere for when to send/resend (send when all acks return, resend when timeout)

    def writable(self):
        print "Writable -> ", bool(self.packReq and self.canWrite)
        return bool(self.packReq and self.canWrite)

    def handle_write(self):
        print "handle_write sending..."

        #for loop to send one group of cwnd# of packets
        for i in self.cwnd:
            self.send(struct.pack('L60s', (self.ackSeq + i), ''))

        self.canWrite = False
        self.packetController()

    def packetController(self):
        

if __name__ == '__main__':

    add = input("Enter IP address of server in single quotes:\n")
    s = Server(add, 8080)

    asyncore.loop() #(0)
