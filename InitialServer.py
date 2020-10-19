# import socket module
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server socket
serverSocket.bind(('localhost', serverPort)) 
serverSocket.listen(1)

while True:
	# Establish the connection
	print("Ready to serve...")
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(1024).decode()
		print("Server receive: ", message)
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()
		#Send one HTTP header line in socket
		connectionSocket.sendall("HTTP/1.1 200 OK\r\n\r\n".encode('utf-8'))
		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.sendall(outputdata[i].encode('utf-8'))
		connectionSocket.close()
	except IOError:
		#Send response message for file not found
		connectionSocket.sendall("HTTP/1.1 404 Not Found\r\n\r\n".encode('utf-8'))
		#Close client socket
		connectionSocket.close()
serverSocket.close()