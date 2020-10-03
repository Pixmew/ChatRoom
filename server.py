import socket
import json
import select
import re


#size of heder which stores length of message
header = 10
d = " Connection aquired, You are now Connected to Server As a Chatter/Message Sender"
#create the server of stream type in ip4 format
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ip = socket.gethostbyname("localHost")
host = 3333
print("connect to -->   Ip : "+ str(ip) + "  Host : " + str(host))
#created server gets bind to ip and port
serversocket.bind((ip,host))
#sets que for sending and reciving data
serversocket.listen(5)



chatterList = [serversocket]
seerList = []
User = {}
Intermidiatemsg = {}


#Function which recieve msg from client and parse it
def ReciveMessage(client_socket):
    try:
        msg = client_socket.recv(header)
        msg_len = int(msg.decode().strip())
        if not msg_len:
            return False
        msg = client_socket.recv(msg_len)
    except:
        return False
    return {"Header":str(msg_len) , "Data":msg.decode()}



#continously check of avalible of clients
while True:
    client_server , _ , client_exception = select.select(chatterList,[],chatterList)
    #get Valid client
    for notified_client in client_server:

        #If there are any new connection accept that connection
        if notified_client == serversocket:
            client_socket , address = serversocket.accept()
            msg = ReciveMessage(client_socket)
            type = client_socket.recv(header)
            type = type.decode().strip()
            if type == "chat":
                chatterList.append(client_socket)
                User[address] = msg
            elif type == "seer":
                seerList.append(client_socket)
                User[address] = msg
            print(msg["Data"] + " is Connected as " + type)
        else:
            msg  = ReciveMessage(notified_client)
            #checks if message is revcieved correctly
            if msg is False:
                continue

            info = str(notified_client)
            ipport = re.search(r"raddr=(\(.*\))" , info)
            Intermidiatemsg["user"] = User[eval(ipport[1])]
            Intermidiatemsg["message"] = msg
            msg = "{:<10}{}".format(len(str(Intermidiatemsg)) , Intermidiatemsg)
            for seerClient in seerList:
                seerClient.send(msg.encode())
