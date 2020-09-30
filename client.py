import socket

header = 10

#creates the socket connection
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#connects the sockets to designeted ip and port
s.connect(("127.0.0.1",3333))

full_msg = ""
newmsg = True
while True:
    #Recive message from server
    msg = s.recv(10)

    #checks if new stream is a new message
    if newmsg:
        full_msg = ""
        msg_size = int(msg.decode().strip())
        newmsg = False
    #concatnates the string untill full mesage is recived and save full message
    full_msg += msg.decode()
    #if full message is recived then print message
    if len(full_msg)-header == msg_size:
        print(full_msg[header:])
        newmsg = True
