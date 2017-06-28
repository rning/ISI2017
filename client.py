import asyncore, socket

class Client(asyncore.dispatcher_with_send):

    def __init__(self, host, port, message):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        self.outBuffer = message

    def handle_close(self):
        print "Client: Connection Closed"
        self.close()

    def handle_read(self):
        print "Received: ", self.recv(1024)
        self.close()

add = input("Enter IP address of server in single quotes:\n")
c = Client(add, 8080, "Hello, !!!")
asyncore.loop()
