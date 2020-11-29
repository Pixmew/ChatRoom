import tkinter
import server
import client

# Create a Main Window for GUI
MainWindow = tkinter.Tk(className = "Chatroom menu")
MainWindow.geometry("600x300")
#Main Title menu bar
menu = tkinter.Menu(MainWindow);MainWindow.config(menu = menu)
clients = None
Name,Ip,Port = None,None,None

#Buttons functions
def serverCreate():
    chatServer = server.Server()
    chatServer.start()


def joinServer():
    clientWindow = tkinter.Toplevel(MainWindow , width = 400 , height = 500)
    clientWindow.title("ChatRoom")
    textCons = tkinter.Text(clientWindow, width = 20, height = 2, bg = "#17202A", fg = "#EAECEE", font = "Helvetica 14", padx = 5, pady = 5)
    textCons.place(relheight =0.745 , rely = 0.08 , relwidth = 1)
    labelBottom = tkinter.Label(clientWindow ,height = 80)
    labelBottom.place(relwidth = 1, rely = 0.825)
    entryMsg = tkinter.Entry(labelBottom)
    entryMsg.place(relwidth = 0.74,relheight = 0.06, rely = 0.008, relx = 0.011)
    entryMsg.focus()
    buttonMsg = tkinter.Button(labelBottom, text = "Send", font = "Helvetica 10 bold",  width = 20, bg = "#ABB2B9")
    buttonMsg.place(relx = 0.77, rely = 0.008, relheight = 0.06,  relwidth = 0.22)

    scrollbar = tkinter.Scrollbar(textCons)
    scrollbar.place(relheight = 1 , relx = 0.974)
    scrollbar.config(command = textCons.yview)
    #textCons.config(state = tkinter.ENABLED)
    clientWindow.mainloop()

#Creating Menu Elements
ConnectionMenu = tkinter.Menu(menu)
#adding menu elements
menu.add_cascade(label = "Connection" , menu = ConnectionMenu)
menu.add_command(label = "Exit" , command = MainWindow.quit)
ConnectionMenu.add_command(label = "Create" , command = serverCreate)
ConnectionMenu.add_command(label = "Join" , command = joinServer)

createButton = tkinter.Button(MainWindow , text = "Create Server" , command = serverCreate)
createButton.place(x = 370 , y = 190)
namelable = tkinter.Label(MainWindow , text = "Name")
namelable.place(x = 30 , y = 50)
name = tkinter.Entry(MainWindow)
name.place(x = 120 , y = 50)

iplable = tkinter.Label(MainWindow , text = "IP")
iplable.place(x = 30 , y = 90)
ip = tkinter.Entry(MainWindow)
ip.place(x = 120 , y = 90)

portlable = tkinter.Label(MainWindow , text = "Port")
portlable.place(x = 30 , y = 130)
port = tkinter.Entry(MainWindow)
port.place(x = 120 , y = 130)
joinButton = tkinter.Button(MainWindow , text = "Join Server" , command = joinServer)
joinButton.place(x = 150 , y = 190)

#End of loop of GUI
MainWindow.mainloop()
