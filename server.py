import asyncore, socket

class Server(asyncore.dispatcher):
    def __init__(self, host, port):
        asycore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((host, port))
        self.listen(1)

    def handle_accept(self):
        socket, address = self.accept()
        print "Server: Connection by ", address
        socket.send(outBuffer)

s = Server("", 8080)
asyncore.loop()
    
