# Author: Shittu Maroof Ayotunde 2014/1/50669CT
from socket import *

# this is the 'localhost' ip address which means the server is on the same machine
serverName = '127.0.0.1' # this allows me to test it on my machine 
serverPort = 22595



clientSocket = socket(AF_INET, SOCK_DGRAM) # creating a socket called clientSocket

message = [] # this list(array) will be used to collect all the information we need to send

# ask for a number to represent which  math operation to be performed
operator = input("""
        WELCOME to my Math Server!! 
        What Operation would you like perform - ?       
                [1] Addition
                [2] Subtraction
                [3] Multiplication 
                [4] Division
                [5] Modulus
                >>>_
                """)
# add it as a string to the first element of the 'message' list
message.append(str(operator)) # str() is used to cast an object to string

# ask for the first and second operands - this program only performs simple binary operations
operand1 = str(input("enter  the first operand: >>>_ ")) # cast the input to string
operand2 = str(input("enter the second oprand: >>>_ ")) # same as operand 1

message.append(operand1) # add the first operand to the message list
message.append(operand2) # add the second one as well


message = " ".join(message) 


clientSocket.sendto(message, (serverName, serverPort))
result, serverAddress = clientSocket.recvfrom(4096) 
print ("the server says:>>> " + result)
clientSocket.close()
