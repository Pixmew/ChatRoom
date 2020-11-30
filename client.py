import socket
import threading

class Client():
    header = None
    s = None
    user = ""
    def __init__(self ,ip , host , name):
        self.header = 10
        user = name
        #creates the socket connection
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #connects the sockets to designeted ip and port
        self.s.connect((ip,int(host)))
        print(socket.gethostname())
        Firstmsg = "{:<10}".format(len(user)) + user + "   chat   "
        self.s.send(Firstmsg.encode())

    def sendMsg(self,msg):
        msg_len = len(msg.strip())
        msg = "{:<10}{} : {}".format((msg_len+len(self.user) + 3),self.user,msg)
        self.s.send(msg.encode())

    def ChatView(self):
        msg = self.s.recv(self.header)
        if len(msg) <= 0:
            return None

        else:
            msg_len = int(msg.decode().strip())
            msg = self.s.recv(msg_len)
            msg_dict = eval(msg.decode())

            return msg_dict["user"]["Data"] + msg_dict["message"]["Data"]
