import socket as sock, sys, getopt, errno

def main(argv):

    verbose = False
    port = 10000;
    server = "localhost"

    try:
        opts, args = getopt.getopt(argv, "vp:s:",["message=","port=","server="])
    except getopts.GetoptError:
        print "Usage: python " + sys.argv[0] + " [-p port -s server]"
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-v":
            verbose = True;
        elif opt in ("-p", "--port"):
            port = int(arg)
        elif opt in ("-s", "--server"):
            server = arg

    server_address = (server, port)
    socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)

    print "starting up server at %s on port %s" % server_address
    try:
        socket.bind(server_address)
    except sock.error as error:
        if error.errno == errno.EADDRINUSE:
            print "Error: Port already in use"
            exit(2)
        else:
            raise
        
    socket.listen(1)

    while True:
        print "waiting for a connection"
        
        connection, client_address = socket.accept()
        
        try:
            data = "dummy"
            while data:
                data = connection.recv(16)
                print "received " + str(len(data)) + " bytes"
                print "sending back"
                connection.sendall(data)
        finally:
            connection.close()
            
if __name__ == "__main__":
    main(sys.argv[1:])
