from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('localhost',serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
     connectionSocket, addr = serverSocket.accept()
     print("TCP connection established")
     sentence = connectionSocket.recv(1024).decode()
     print("Server receive: ", sentence)
     capitalizedSentence = sentence.upper()
     print("Server send: ", capitalizedSentence)
     connectionSocket.send(capitalizedSentence.encode())
     print(connectionSocket)
     connectionSocket.close()