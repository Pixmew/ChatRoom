import tkinter
import server

# Create a Main Window for GUI
MainWindow = tkinter.Tk(className = "Chatroom")

#function for Creat server
def CreateServer():
    ChatServer = server.Server()
    ChatServer.serverCreate()


createButton = tkinter.Button(MainWindow , text = "Create" , activebackground = "#999" , command = CreateServer)
createButton.pack()

joinButton = tkinter.Button(MainWindow , text = "Join" , activebackground = "#999")
joinButton.pack()


#End of loop of GUI
MainWindow.mainloop()
