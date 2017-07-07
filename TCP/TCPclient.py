import asyncore, socket

class Client(asyncore.dispatcher_with_send):

    def __init__(self, host, port, message):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        self.buffer = message

    def handle_close(self):
        print "Client: Connection Closed"
        self.close()

    def readable(self):
        return True

    def handle_read(self):
        print "Received: ", self.recv(8192)

    def writeable(self):
        return bool(len(self.buffer) > 0)

    def handle_write(self):
        self.send(self.buffer)

add = input("Enter IP address of server in single quotes:\n")
c = Client(add, 8080, "Test message")
asyncore.loop()
