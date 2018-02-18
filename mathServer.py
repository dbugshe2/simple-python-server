from socket import *

serverPort = 220595 




serverSocket = socket(AF_INET, SOCK_DGRAM)


serverSocket.bind(('', serverPort))
print("The server is ready to recieve")

# this is the calculator code

# these number stand for the operations we will be performing
ADDITION = 1
SUBTRACTION = 2
MULTIPLICATION = 3
DIVISION = 4
MODULUS = 5

def calculator(message): # the actual calculator function
    """
    takes in a message string that contains an operation as the first number
    and two operands as the second and the third
    and returns the result of the operation on them
    """
    # here we split the message string back to a list
    message = message.split(',') # the split function create a list(array)  from a string
    
    # we seperate the different parts of the message
    operator =  int(message[0]) 
    operand1 = int(message[1])
    operand2 = int(message[2])
    
    
    # based what number the operator variable is we will perform the right operation
    # or else return some kind of error message
    if(operator == ADDITION):
        return operand1 + operand2
    elif(operator == SUBTRACTION):
        return operand1 - operand2
    elif(operator == MULTIPLICATION):
        return operand1 * operand2
    elif(operator == DIVISION ):
        return operand1 / operand2
    elif(operator == MODULUS):
        return operand1 % operand2
    else:
        return ' error: no valid operation'

while 1: 
    
    message, clientAddress = serverSocket.recvfrom(4096)
    
    resultMessage = str(calculator(message))
    serverSocket.sendto(resultMessage, clientAddress)
