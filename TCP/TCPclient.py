import asyncore, socket, struct
#from ParameterParser import *

class Client(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        self.packetLength = 32

        self.seq = 0
        self.ack = 0

    def handle_close(self):
        print "Client: Connection Closed"
        self.close()

    def handle_read(self):
        print "handle_read reading..."

        readBuffer = self.recv(4096)
        print str(len(readBuffer))
        
        for i in range(0, len(readBuffer) / 32):
            #unpack structure sent from server: [seq,ack,string]
            packet = struct.unpack('LL24s', readBuffer[:32]) #size: 32 bytes
            print 'received packet with seq#' , packet[0], 'ack#', packet[1] 

            #increment ACK based on receieved pack seq
            #send ACK immediately for each pack recieved
            if packet[0] == (self.ack + 1):
                self.ack += 1
                #pack structure and send to server: [seq,ack,string]
                self.send(struct.pack('LL24s', self.seq, self.ack, 'data'))
                print 'sending ack'
            else:
                self.ack = packet[0] # For retransmit, if it is out of sync, resync self.ack
                self.send(struct.pack('LL24s', self.seq, self.ack, 'data'))
                print 'redefined ack, sending ack'

            readBuffer = readBuffer[32:]

if __name__ == '__main__':

    address = str(input("Enter IP address of server in single quotes:\n"))
    c = Client(address, 8080)

    asyncore.loop(0)
