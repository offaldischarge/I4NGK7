import sys
import socket

HOST = "10.0.0.1"
PORT = 9000

def main(argv):

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind((HOST, PORT))

    while True:
        print('Server ready to receive')
        data, addr = serverSocket.recvfrom(1024)
        message = data.decode().upper()

        if message == "U":
            file = open("/proc/uptime", "r")
            uptime = file.read()
            uptimeStr = convertTuple(uptime)
            serverSocket.sendto(uptimeStr.encode(), (addr[0], addr[1]))
            file.close()
        elif message == "L":
            file = open("/proc/loadavg", "r")
            loadavg = file.read()
            loadavgStr = convertTuple(loadavg)
            serverSocket.sendto(loadavgStr.encode(), (addr[0], addr[1]))
            file.close()

    serverSocket.close()

def convertTuple(tup): 
    str =  ''.join(tup) 
    return str            

if __name__ == "__main__":
   main(sys.argv[1:])