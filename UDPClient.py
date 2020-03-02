import sys
import socket
from lib import Lib

PORT = 9000
BUFSIZE = 1000

def main(argv):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    clientSocket.sendto("l", (10.0.0.1, 9000))

if __name__ == "__main__":
   main(sys.argv[1:])