import asyncore, socket
from ParameterParser import *

def incrementData(data, factor, initcwnd=10, recentACK=0):
    # WIP, assumed that this is the first send, increment
    ackNum = recentACK + 1
    incrementAmt = initcwnd ** ackNum # raise the initial amount to the most recent sent ACK
    data = data * incrementAmt # multiply the string by that amount to simulate multiple packets
    return data

class Server(asyncore.dispatcher):

    def __init__(self, host, port, message):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((host, port))
        self.listen(5)
        self.outBuffer = message
        print "Server: Waiting for connection..."

    def handle_close(self):
        print "Server: Closed"
        self.close()

    def handle_accept(self):
        self.sock, self.address = self.accept()
        print "Server: Connection by ", self.address
        self.sock.setblocking(0)
        self.sock.send(self.outBuffer)
        EchoServer(self.sock)

class EchoServer(asyncore.dispatcher):

    def __init__(self, sock):
        asyncore.dispatcher.__init__(self, sock=sock)
        self.outBuffer = "testbufferwhodis"

    def readable(self):
        print "Readable -> True"
        return True

    def handle_read(self):
        print "handle_read reading..."
        print "Received: ", self.recv(1024)

    def writable(self):
        print "Writable -> ", bool(self.outBuffer)
        return bool(self.outBuffer)

    def handle_write(self):
        print "handle_write sending..."
        sent = self.send(self.outBuffer)
        self.outBuffer = self.outBuffer[sent:]

if __name__ == '__main__':

    add = input("Enter IP address of server in single quotes:\n")
    s = Server(add, 8080, "Server connected. Send/Receive active.")

    asyncore.loop()
