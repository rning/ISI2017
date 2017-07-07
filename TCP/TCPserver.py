import asyncore, socket

class Server(asyncore.dispatcher_with_send):
    def __init__(self, host, port, message):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((host, port))
        self.listen(1)
        self.outBuffer = message
        print "Server: Waiting for connection..."

    def handle_close(self):
        print "Server: Closed"
        self.close()

    def handle_accept(self):
        socket, address = self.accept()
        print "Server: Connection by ", address
        socket.send(self.outBuffer)

    def readable(self):
        print "Readable -> True"
        return True

    def handle_read(self):
        print "Received: ", self.recv(1024)

    def writable(self):
        print "Writable -> ", bool(self.outBuffer)
        return bool(self.outBuffer)
        if bool(self.outBuffer) == True:
            self.handle_write() 

    def handle_write(self):
        print "handle_write sending..."
        sent = self.socket.send(self.outBuffer)
        self.outBuffer = self.outBuffer[sent:]

add = input("Enter IP address of server in single quotes:\n")
s = Server(add, 8080, "Server connected. Send/Receive active.")

asyncore.loop()
