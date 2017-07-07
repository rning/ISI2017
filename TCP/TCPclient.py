import asyncore, socket

class Client(asyncore.dispatcher_with_send):

    def __init__(self, host, port, message):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        self.outBuffer = message

    def handle_close(self):
        if recv(1024) == 0:
            print "Client: Connection Closed"
            self.close()
        else:
            self.handle_read()

    def readable(self):
        print "Readable -> True"
        return True

    def handle_read(self):
        print "Received: ", self.recv(1024)

    def writable(self):
        print "Writable -> True"
        return bool(self.outBuffer)

    def handle_write(self):
        print "handle_write sending..."
        sent = self.socket.send(self.outBuffer)
        self.outBuffer = self.outBuffer[sent:]

address = input("Enter IP address of server in single quotes:\n")
c = Client(address, 8080, "Test message")
asyncore.loop()
