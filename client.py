from socket import *

# this is the 'localhost' ip address which means the server is on the same machine
serverName = '127.0.0.1' # you may change this if you're using another computer as the server
serverPort = 15000 # a random port number chosen for this process

# The AF_INET argument means were making use of the internet
# The SOCK_DGRAM argument menas we're creating a Datagram Sock (UDP Socket)
clientSocket = socket(AF_INET, SOCK_DGRAM) # creating a socket called clientSocket

message = [] # this list(array) will be used to collect all the information we need to send

# ask for a number to represent which math operation to be performed
operator = input("""
                WELCOME to my Math Server!!
                What Operation would you like perform?
                (1) Addition    (2) Subtraction
                (3) Multiplication  (4) Division
                >>>_
                """)
# add it as a string to the first element of the 'message' list
message.append(str(operator)) # str() is used to cast an object to string

# ask for the first and second operands - this program only performs simple binary operations
operand1 = str(input("enter  the first operand: >>>_ ")) # cast the input to string
operand2 = str(input("enter the second oprand: >>>_ ")) # same as operand 1

message.append(operand1) # add the first operand to the message list
message.append(operand2) # add the second one as well

# the join() function converts our list to a string and saves it as the new value of message
message = " ".join(message) 

# the sendto() function sends our message to the server

# (1) the first argument of the sendto() is the message itself as a string, sending it as another data-type may generate errors
# NB: We send string because they are bytes-like and you can only send bytes through the network

# the second argument (in parenthises) is the the socket we want to send the message to

clientSocket.sendto(message, (serverName, serverPort))
# then we wait for a response 

# the recvfrom() function listens for a response from the server
# the response is saved in the result variable ,along with the address of the server it came from
result, serverAddress = clientSocket.recvfrom(4096) # 4096 here is the buffer size of the socket(in bytes)
print ("the server returned " + result) # here ew print the result
clientSocket.close() # and we close the client socket
