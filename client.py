import socket

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
        self.s.connect((socket.gethostname(),int(host)))
        print(socket.gethostname())
        Firstmsg = "{:<10}".format(len(user)) + user + "   chat   "
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
            msg = "{:<10}{} : {}".format((msg_len+len(user) + 3),user,msg)
            s.send(msg.encode())
