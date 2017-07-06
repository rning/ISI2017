import asyncore, socket

class Client(asyncore.dispatcher_with_send):

    def __init__(self, host, port, message):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
<<<<<<< HEAD
        self.outBuffer = message
=======
        message = self.outBuffer
>>>>>>> 5cdc185d99bb68aa20d988f9364aa9f8da771be8

    def handle_close(self):
        print "Client: Connection Closed"
        self.close()

    def readable(self):
        return True

    def handle_read(self):
        print "Received: ", self.recv(1024)

    def writeable(self):
        return bool(self.outBuffer)

    def handle_write(self):
        self.send(self.outBuffer)

add = input("Enter IP address of server in single quotes:\n")
c = Client(add, 8080)
asyncore.loop()
