import asyncore, socket

class Server(asyncore.dispatcher_with_send):
    def __init__(self, host, port, message):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((host, port))
        self.listen(1)
        self.buffer = message
        print "Server: Waiting for connection..."

    def handle_close(self):
        print "Server: Closed"
        self.close()

    def handle_accept(self):
        socket, address = self.accept()
        print "Server: Connection by ", address
        #self.send(self.outBuffer)

    def readable(self):
        return True

    def handle_read(self):
        print "Received: ", self.recv(1024)

    def writeable(self):
        return bool(self.outBuffer) 

    def handle_write(self):
        self.send(self.outBuffer)

add = input("Enter IP address of server in single quotes:\n")
s = Server(add, 8080, "Server connected. Send/Receive active.")

asyncore.loop()

