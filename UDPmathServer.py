# Author: Shittu Maroof Ayotunde 2014/1/50669CT
from socket import *
import math

serverPort = 22595




serverSocket = socket(AF_INET, SOCK_DGRAM)


serverSocket.bind(('', serverPort))
print("The server is now running and is ready to recive")

# this is the calculator code

# these number stand for the operations we will be performing
SINE = 1
COSINE = 2
TANGENT = 3
SQUARE_ROOT = 4
FACTORIAL = 5

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
    operand = int(message[1])


    # based what number the operator variable is we will perform the right operation
    # or else return some kind of error message
    if(operator == SINE):
        return math.sin(operand)
    elif(operator == COSINE):
        return math.cos(operand)
    elif(operator ==  TANGENT):
        return math.tan(operand)
    elif(operator == SQUARE_ROOT ):
        return math.sqrt(operand)
    elif(operator == FACTORIAL):
        return math.factorial(operand)
    else:
        return ' error: no valid operation'

while True:
    message, clientAddress = serverSocket.recvfrom(4096)
    print("calculating the result for client "+ clientAddress)
    resultMessage = str(calculator(message))
    serverSocket.sendto(resultMessage, clientAddress)
