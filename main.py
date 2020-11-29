import tkinter
import server
import client

# Create a Main Window for GUI
MainWindow = tkinter.Tk(className = "Menu")
MainWindow.geometry("400x300")
#Main Title menu bar
menu = tkinter.Menu(MainWindow);MainWindow.config(menu = menu)
clients = None


#Buttons functions
def serverCreate():
    chatServer = server.Server()
    chatServer.start()


def joinServer():
    pass


#Creating Menu Elements
ConnectionMenu = tkinter.Menu(menu)
#adding menu elements
menu.add_cascade(label = "Connection" , menu = ConnectionMenu)
menu.add_command(label = "Exit" , command = MainWindow.quit)
ConnectionMenu.add_command(label = "Create" , command = serverCreate)
ConnectionMenu.add_command(label = "Join" , command = joinServer)

createButton = tkinter.Button(MainWindow , text = "Create Server" , command = serverCreate)
createButton.pack()
joinButton = tkinter.Button(MainWindow , text = "Join Server" , command = joinServer)
joinButton.pack()

#End of loop of GUI
MainWindow.mainloop()
