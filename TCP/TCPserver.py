import asyncore, socket

class Server(asyncore.dispatcher):
    def __init__(self, host, port, message):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((host, port))
        self.listen(5)
        self.outBuffer = message
        self.isConnected = False
        print "Server: Waiting for connection..."

    def handle_close(self):
        print "Server: Closed"
        self.close()

    def handle_accept(self):
        self.sock, self.address = self.accept()
        print "Server: Connection by ", self.address
        self.sock.setblocking(0)
        self.sock.send(self.outBuffer)
        self.isConnected = True
        
    def readable(self):
        print "Readable -> True"
        return True

    def handle_read(self):
        print "handle_read reading..."
        print "Received: ", self.sock.recv(1024)

    def writable(self):
        print "Writable -> ", bool(self.outBuffer and self.isConnected)
        return bool(self.outBuffer and self.isConnected)

    def handle_write(self):
        print "handle_write sending..."
        sent = self.sock.send(self.outBuffer)
        self.outBuffer = self.outBuffer[sent:]
    
#    def change_data(self, data):
#        self.outBuffer += data # add more data rather than using socket.send by itself and let handle_write handle it
        
add = input("Enter IP address of server in single quotes:\n")
s = Server(add, 8080, "Server connected. Send/Receive active.")

asyncore.loop()
