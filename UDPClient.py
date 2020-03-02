import sys
import socket

SERVERPORT = 9000

def main(argv):
    serverName = sys.argv[1]
    serverArg = sys.argv[2]

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSocket.settimeout(1)
    clientSocket.sendto(serverArg.encode(), (serverName, SERVERPORT))
    
    try:
        data, adrr = clientSocket.recvfrom(1024)
        print(data.decode())
    except socket.timeout:
        print('Request timed out')
    
    clientSocket.close()

if __name__ == "__main__":
   main(sys.argv[1:])