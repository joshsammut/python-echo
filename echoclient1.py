import socket as SOCKET, sys, getopt

def main(argv):

    verbose = False
    message = "Echo"

    try:
        opts, args = getopt.getopt(argv, "vm:",["message="])
    except getopts.GetoptError:
        print "Usage: python " + sys.argv[0] + " [-m message]"
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-v":
            verbose = True;
        elif opt in ("-m", "--message"):
            message = arg;
    
    socket = SOCKET.socket(SOCKET.AF_INET, SOCKET.SOCK_STREAM)
    server_address = ("localhost", 10000)
    
    print "connecting to %s on port %s" % server_address
    socket.connect(server_address)
    
    try:
        print "sending..."
        socket.sendall(message)
        
        amount_received = 0
        amount_expected = len(message)
        received_message = ""
        
        while amount_received < amount_expected:
            data = socket.recv(16)
            amount_received += len(data)
            received_message += data
        print received_message
        
    finally:
        print "closing socket"
        socket.close()

if __name__ == "__main__":
    main(sys.argv[1:])
