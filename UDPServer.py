from socket import *

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('localhost', serverPort))
print 'The server is ready to receive'
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print "Server receive: ", message
    modifiedMessage = message.decode().upper()
    print "Server send: ", modifiedMessage 
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)

