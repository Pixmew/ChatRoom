import tkinter
import Connections

# Create a Main Window for GUI
MainWindow = tkinter.Tk(className = "Chatroom")
#Main Title menu bar
menu = tkinter.Menu(MainWindow);MainWindow.config(menu = menu)


#Creating Menu Elements
ConnectionMenu = tkinter.Menu(menu)

#adding menu elements
menu.add_cascade(label = "Connection" , menu = ConnectionMenu)

ConnectionMenu.add_command(label = "Create" ,command = Connections.CreateServer)


createButton = tkinter.Button(MainWindow , text = "Create" , activebackground = "#999" , command = Connections.CreateServer)
createButton.pack()

joinButton = tkinter.Button(MainWindow , text = "Join" , activebackground = "#999")
joinButton.pack()


#End of loop of GUI
MainWindow.mainloop()
