import sys
import socket

HOST = '10.0.0.1'
PORT = 9000
BUFSIZE = 1000

def main(argv):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind((HOST, PORT))
    
    while True:
        data, addr = serverSocket.recvfrom(1024)
        print('Received message: ', data)

if __name__ == "__main__":
   main(sys.argv[1:])