import socket

class Client():
    header = None
    s = None
    User = ""
    def __init__():
        self.header = 10
        #creates the socket connection
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #connects the sockets to designeted ip and port
        self.s.connect(("localHost",ip))
        self.User = input("Enter Your Name : ")
        Firstmsg = "{:<10}".format(len(User)) + User + "   chat   "
        self.s.send(Firstmsg.encode())

    def msgReciver():
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


    def MsgSender():
        while True:
            msg = input("{}  ->  ".format(User))
            msg_len = len(msg.strip())
            if msg_len == 0:
                print("msg not sent")
                continue
            msg = "{:<10}{} : {}".format((msg_len+len(User) + 3),User,msg)
            s.send(msg.encode())
