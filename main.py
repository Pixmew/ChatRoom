import tkinter
import server
import client

# Create a Main Window for GUI
MainWindow = tkinter.Tk(className = "Chatroom")
MainWindow.geometry("400x300")
#Main Title menu bar
menu = tkinter.Menu(MainWindow);MainWindow.config(menu = menu)
clients = None


#Creating Menu Elements
ConnectionMenu = tkinter.Menu(menu)
#adding menu elements
menu.add_cascade(label = "Connection" , menu = ConnectionMenu)
menu.add_command(label = "Exit" , command = MainWindow.quit)
ConnectionMenu.add_command(label = "Create" ,command = )
ConnectionMenu.add_command(label = "Join")


createButton = tkinter.Button(MainWindow , text = "Create" , activebackground = "#999" , command = CreateServer)
createButton.pack()


joinButton = tkinter.Button(MainWindow , text = "Join" , activebackground = "#999" , command = connect)
joinButton.pack()


#End of loop of GUI
MainWindow.mainloop()
