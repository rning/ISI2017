import asyncore, socket

class Server(asyncore.dispatcher_with_send):
    def __init__(self, host, port, message):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((host, port))
        self.listen(1)
        self.outBuffer = message
        print "Server: Waiting for connection..."

    def handle_accept(self):
        socket, address = self.accept()
        print "Server: Connection by ", address
        socket.send(self.outBuffer)
    
    def handle_close(self):
        print "Server: Closed"
        self.close()

add = input("Enter IP address of server in single quotes:\n")
s = Server(add, 8080, "Server says hello!!!")
asyncore.loop()
