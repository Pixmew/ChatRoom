import tkinter

# Create a Main Window for GUI
MainWindow = tkinter.Tk(className = "Chatroom")

createButton = tkinter.Button(MainWindow , text = "Create" , activebackground = "#999")
createButton.pack()

joinButton = tkinter.Button(MainWindow , text = "Join" , activebackground = "#999")
joinButton.pack()

#End of loop of GUI
MainWindow.mainloop()
