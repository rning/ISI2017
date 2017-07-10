import asyncore, socket

class Client(asyncore.dispatcher):

    def __init__(self, host, port, message):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        self.outBuffer = message
        self.isConnected = False

    def handle_close(self):
        print "Client: Connection Closed"
        self.close()
        
    def handle_connect(self):
        print "handle_connect called"
        self.isConnected = True

    def readable(self):
        print "Readable -> True"
        return True

    def handle_read(self):
        print "handle_read reading..."
        print "Received: ", self.recv(1024)

    def writable(self):
        print "Writable -> ", bool(self.outBuffer and self.isConnected)
        return bool(self.outBuffer and self.isConnected)

    def handle_write(self):
        print "handle_write sending..."
        sent = self.send(self.outBuffer)
        self.outBuffer = self.outBuffer[sent:]

address = input("Enter IP address of server in single quotes:\n")
c = Client(address, 8080, "Test message")
asyncore.loop()
