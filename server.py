import asyncore, socket

class Server(asyncore.dispatcher_with_send):
    def __init__(self, host, port, message):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((host, port))
        self.listen(1)
        self.outBuffer = message
        print "Server: Waiting for commection..."

    def handle_accept(self):
        socket, address = self.accept()
        print "Server: Connection by ", address
        socket.send(outBuffer)

add = input("Enter IP address of server in single quotes:\n")
s = Server(add, 8080, "Server says hello!!!/n")
asyncore.loop()
    
