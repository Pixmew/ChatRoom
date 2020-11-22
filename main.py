import tkinter
import Connections

# Create a Main Window for GUI
MainWindow = tkinter.Tk(className = "Chatroom")
MainWindow.geometry("400x300")
#Main Title menu bar
menu = tkinter.Menu(MainWindow);MainWindow.config(menu = menu)


#Creating Menu Elements
ConnectionMenu = tkinter.Menu(menu)

#adding menu elements
menu.add_cascade(label = "Connection" , menu = ConnectionMenu)
menu.add_command(label = "Exit" , command = MainWindow.quit)

ConnectionMenu.add_command(label = "Create" ,command = Connections.CreateServer)
ConnectionMenu.add_command(label = "Join")

createButton = tkinter.Button(MainWindow , text = "Create" , activebackground = "#999" , command = Connections.CreateServer)
createButton.pack()

joinButton = tkinter.Button(MainWindow , text = "Join" , activebackground = "#999")
joinButton.pack()


#End of loop of GUI
MainWindow.mainloop()
