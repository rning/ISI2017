import asyncore, socket

class Client(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))

    def handle_close(self):
        print "Client: Connection Closed"
        self.close()

    def handle_read(self):
        print "Received: ", self.recv(1024)
        self.handle_close()

add = input("Enter IP address of server in single quotes:\n")
c = Client(add, 8080)
asyncore.loop()
