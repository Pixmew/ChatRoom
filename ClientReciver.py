import socket
import json

header = 10
#creates the socket connection
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#connects the sockets to designeted ip and port
server = ("localHost",3333)
s.connect(server)
User = input("Enter Your Name : ")
Firstmsg = "{:<10}".format(len(User)) + User + "   seer   "
s.send(Firstmsg.encode())

while True:
    msg = s.recv(header)
    if msg == False:
        continue
    else:
        msg_len = int(msg.decode().strip())
        msg = s.recv(msg_len)
        msg_dict = eval(msg.decode())

        print("-"*30)
        print(msg_dict["user"]["Data"] + "  --->\n\n" + msg_dict["message"]["Data"])
        print("-"*30)
