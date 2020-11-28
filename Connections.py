import server
import client

#function for Creat server
def CreateServer():
    ChatServer = server.Server()
    ChatServer.start()

#function to join a server
def JoinServer(ip , host , name):
    Client = client.Client(ip , host , name)
