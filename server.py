import socket
import pickle

#size of heder which stores length of message
header = 10
d = {34:"sdiuf"}
#create the server of stream type in ip4 format
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostbyname("localHost")
print("connect to : "+ str(ip))
#created server gets bind to ip and port
serversocket.bind((ip,3333))
#sets que for sending and reciving data
serversocket.listen(5)

#continously check of avalible of clients
while True:
    #server connection message
    msg = pickle.dumps(d)
    #accept all clients
    clientsocket,address = serversocket.accept()
    #concatnate the message with the size of msg in advanced
    msg  = bytes("{:<{header}}".format(len(msg),header = header),"utf-8") + msg
    print(msg)
    print(f"Connection from {address} has been Established!")
    #send updated message to client
    clientsocket.send(msg.encode())
