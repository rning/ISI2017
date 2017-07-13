import asyncore, socket, struct
#from ParameterParser import *

class Client(asyncore.dispatcher):

    def __init__(self, host, port, packReq):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        self.packReq = packReq
        self.outBuffer = "" #
        self.packSeq = 0
        self.isConnected = False

    def handle_close(self):
        print "Client: Connection Closed"
        self.close()
        
    def handle_connect(self): #sends packReq
        print "handle_connect called"
        self.isConnected = True
        self.send(struct.pack('LL', 0, packReq))

    def readable(self):
        print "Readable -> True"
        return True

    def handle_read(self):
        print "handle_read reading..."

        #unpack structure sent from server: [pack seq, data (should be large # of bytes)]
        recPack = struct.unpack('L60s', self.recv(4096)) #size: 64 bytes
        
        #increment ACK based on receieved pack seq
        #send ACK immediately for each pack recieved (presumably within handle_read, but maybe with handle_write)
        if recPack[0] == (self.packSeq + 1):
            self.packSeq += 1
            #send here or in handle_write?

    def writable(self):
        print "Writable -> ", bool(self.outBuffer and self.isConnected)
        return bool(self.outBuffer and self.isConnected)

    def handle_write(self): #sends ACKs(?)
        print "handle_write sending..."
        sent = self.send(self.outBuffer)
        self.outBuffer = self.outBuffer[sent:]

if __name__ == '__main__':

    address = input("Enter IP address of server in single quotes:\n")
    c = Client(address, 8080, 100) #packReq

    asyncore.loop() #(0)
