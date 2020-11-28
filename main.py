import tkinter
import server
import client

# Create a Main Window for GUI
MainWindow = tkinter.Tk(className = "Chatroom")
MainWindow.geometry("400x300")
#Main Title menu bar
menu = tkinter.Menu(MainWindow);MainWindow.config(menu = menu)

clients = None
#function for Creat server
def CreateServer():
    ChatServer = server.Server()
    ChatServer.start()

def connect():
    log = tkinter.Toplevel()
    log.geometry("300x300")
    l1 = tkinter.Message(log , text = "Name")
    l1.pack()
    name = tkinter.Entry(log)
    name.pack()

    l2 = tkinter.Message(log , text = "IP")
    l2.pack()
    ip = tkinter.Entry(log)
    ip.pack()

    l3 = tkinter.Message(log , text = "Host")
    l3.pack()
    host = tkinter.Entry(log)
    host.pack()

    def login():
        clients = client.Client(ip.get() , host.get() , name.get())
        
        log.quit()

    submit = tkinter.Button(log , text = "Submit" ,command =login)
    submit.pack()

    log.mainloop()

#Creating Menu Elements
ConnectionMenu = tkinter.Menu(menu)

#adding menu elements
menu.add_cascade(label = "Connection" , menu = ConnectionMenu)
menu.add_command(label = "Exit" , command = MainWindow.quit)

ConnectionMenu.add_command(label = "Create" ,command = CreateServer)
ConnectionMenu.add_command(label = "Join")

createButton = tkinter.Button(MainWindow , text = "Create" , activebackground = "#999" , command = CreateServer)
createButton.pack()

joinButton = tkinter.Button(MainWindow , text = "Join" , activebackground = "#999" , command = connect)
joinButton.pack()


#End of loop of GUI
MainWindow.mainloop()
