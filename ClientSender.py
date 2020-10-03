import socket

header = 10
#creates the socket connection
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#connects the sockets to designeted ip and port
s.connect(("localHost",3333))
User = input("Enter Your Name : ")
Firstmsg = "{:<10}".format(len(User)) + User + "   chat   "
s.send(Firstmsg.encode())
while True:
    msg = input("{}  ->  ".format(User))
    msg_len = len(msg.strip())
    if msg_len <= 0:
        continue
    msg = "{:<10}{}".format(msg_len,msg)
    s.send(msg.encode())
