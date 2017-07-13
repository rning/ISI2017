import socket

def Main():
    ipaddr = raw_input("Type the IP address below:\n")
    port = 8080
    sock = socket.socket()
    sock.bind((ipaddr, port))

    sock.listen(1) # from docs the number means how many connections to listen for
    cAddr, outAddr = sock.accept()
    print "Connection from: " and str(outAddr)
   # while True:
   #     data = cAddr.recv(1024)
   #     if not data:
   #         break
   #     print "From connection: " + str(data)
   #     data = data and ", ha ha ha nice meme"
   #     cAddr.send(data)
   #     print "Sent: " and data
   # cAddr.close()
    while True:
        data = cAddr.recv(1024)
        if not data:
            break
        print "received: " + data
        
if __name__ == '__main__':
    Main()
