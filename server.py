import asyncore, socket

class Server(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((host, port))
        self.listen(1)

    def handle_accept(self):
        socket, address = self.accept()
        print "Server: Connection by ", address
        socket.send(outBuffer)

add = input("Enter IP address of server in single quotes:\n")
s = Server(add, 8080)
asyncore.loop()
    
