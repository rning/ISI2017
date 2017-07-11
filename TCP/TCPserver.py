import asyncore, socket
from ParameterParser import *

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
        EchoServer(self.sock) #this would be es = EchoServer(self.sock)

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

# s.es.outBuffer to reference EchoServer's outBuffer