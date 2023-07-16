#Nick Krisulevicz
#COSC 370
#Socket Programming Assignment 1
#03/07/2022
#socket.py

from socket import * 
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 9876
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

while True :
    print ('Ready to serve ... ')
   
    connectionSocket, addr = serverSocket.accept()
    try :
    
        message = connectionSocket.recv(1024)
        print ('Message is: ', message)

        filename = message.split ()[1]
        print ('Filename is: ', filename)

        f = open ( filename [1:])

        outputdata = f.read()
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        for i in range (0 , len ( outputdata )):
            connectionSocket.send ( outputdata [ i ].encode ())
        
        connectionSocket.send ("\r\n".encode())
        connectionSocket.close ()
    except IOError :
        connectionSocket.send("HTTP/1.1 404 Not Found \r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1><body><html>\r\n".encode())
        
        connectionSocket.close()
sys.exit ()
