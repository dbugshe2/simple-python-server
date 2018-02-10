from socket import *

serverPort = 15000 # a random port number chosen for this process, we should make sure our client and server are using th same port number


# The AF_INET argument means were making use of the internet
# The SOCK_DGRAM argument menas we're creating a Datagram Sock (UDP Socket) 
serverSocket = socket(AF_INET, SOCK_DGRAM)

# then we bind(assign) the port number(serverPort) to the serverSocket process
serverSocket.bind(('', serverPort)) # the first blank argument means that we're using whatever ip address our current machine(localhost) has
print("The server is ready to recieve")

# this is the calculator code you may write it in anyway you can

# these number stand for the operations we will be performing
ADDITION = 1
SUBTRACTION = 2
MULTIPLICATION = 3
DIVISION = 4

def calculator(message): # the actual calculator function
    """
    takes in a message string that contains an operation as the first number
    and two operands as the second and the third
    and returns the result of the operation on them
    """
    # here we split the message string back to a list
    message = message.split(' ') # the split function create a list(array)  from a string
    
    # we seperate the different parts of the message
    operator =  int(message[0]) 
    operand1 = int(message[1])
    operand2 = int(message[2])
    
    
    # based what number the operator variable is we will perform the right operation
    # or else return some kind of error message
    if(operator == ADDITION):
        return operand1 + operand2
    elif(operator == SUBTRACTION):
        return operand2 - operand1
    elif(operator == MULTIPLICATION):
        return operand1 * operand2
    elif(operator == DIVISION ):
        return operand1 / operand2
    else:
        return ' error: no valid operation'

while 1: # an infinte loop to keep the server running and listening for requests
    # the recvfrom() function listens for request in the serverSocket we created ealier
    # and we save the input in the message variable, and the address of the client
    message, clientAddress = serverSocket.recvfrom(4096) # we are using the same number(4096) as buffer size in both the client and server
    
    resultMessage = str(calculator(message)) # we perform the calculation on the message we recived
    serverSocket.sendto(resultMessage, clientAddress) # the sendto() function send back the result to the client address
