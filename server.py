import socket
import json
import select
import re
import random
import threading

class Server(threading.Thread):

    chatterList = []
    seerList = []
    User = {}
    Intermidiatemsg = {}
    serversocket = None
    #size of heder which stores length of message
    header = 10
    d = "New Connection aquired : "

    def InitializeServer(self):
        ip = socket.gethostbyname(socket.gethostname())
        #create the server of stream type in ip4 format
        self.serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        port = random.randint(2000,9999)
        print("Server is now Started\nconnect to -->   Ip : "+ str(ip) + "  Host : " + str(port))
        #created server gets bind to ip and port
        self.serversocket.bind((ip,port))
        #sets que for sending and reciving data
        self.serversocket.listen(5)
        self.chatterList.append(self.serversocket)

    #Function which recieve msg from client and parse it
    def ReciveMessage(self,client_socket):
        try:
            msg = client_socket.recv(self.header)
            msg_len = int(msg.decode().strip())
            if not msg_len:
                return False
            msg = client_socket.recv(msg_len)
        except:
            return False
        return {"Header":str(msg_len) , "Data":msg.decode()}


    def startServer(self):
        #continously check of avalible of clients
        while True:
            client_server , _ , client_exception = select.select(self.chatterList,[],self.chatterList)
            #get Valid client
            for notified_client in client_server:

                #If there are any new connection accept that connection
                if notified_client == self.serversocket:
                    client_socket , address = self.serversocket.accept()
                    msg = self.ReciveMessage(client_socket)
                    type = client_socket.recv(self.header)
                    type = type.decode().strip()
                    if type == "chat":
                        self.chatterList.append(client_socket)
                        self.User[address] = msg
                    elif type == "seer":
                        self.seerList.append(client_socket)
                        self.User[address] = msg
                    print(d + msg["Data"])
                else:
                    msg  = self.ReciveMessage(notified_client)
                    #checks if message is revcieved correctly
                    if msg is False:
                        continue

                    info = str(notified_client)
                    ipport = re.search(r"raddr=(\(.*\))" , info)
                    self.Intermidiatemsg["user"] = self.User[eval(ipport[1])]
                    self.Intermidiatemsg["message"] = msg
                    msg = "{:<10}{}".format(len(str(self.Intermidiatemsg)) , self.Intermidiatemsg)
                    for seerClient in self.seerList:
                        seerClient.send(msg.encode())

    def run(self):
        self.InitializeServer()
        self.startServer()
