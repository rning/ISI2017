import socket

def Main()
    ipaddr = raw_input('Type the IP belown')
    port = 8080

    sock = socket.socket()
    sock.connect((ipaddr, port))
    
    message = raw_input(S E N D T H I N G, exit get me outta heren)
    while message != get me outta here
        sock.send(message)
        received = sock.recv(1024)
        print received from ur ex  and str(received)
        message = raw_input(gimme more stuff to sendn)
    sock.close()

if __name__ == __main__
    Main()