from socket import *

serverPort = 15000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to recieve")

ADDITION = 1
SUBTRACTION = 2
MULTIPLICATION = 3
DIVISION = 4

def calculator(message):
    """
    takes in a collection of operands and performs the
    same operation on them and returns the result
    """
    message = message.split(' ')

    operator =  int(message[0])
    operand1 = int(message[1])
    operand2 = int(message[2])

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

while 1:
    message, clientAddress = serverSocket.recvfrom(4096)
    modifiedMessage = str(calculator(message))
    serverSocket.sendto(modifiedMessage, clientAddress)
