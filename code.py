from tkinter import *
import tkinter as tk

MainWindow = tk.Tk()
MainWindow.geometry("260x160")

def ButtonCommand():
    global Clicks
    Clicks = Clicks+1
    if (Clicks % 2)==0:
        OnOFFButton.config(text = "STOP")
        #add other code
    elif (Clicks % 2)==1:
        OnOffButton.config(text = "START")
        #add other code

Clicks = 1

OnOffButton = tk.Button(
    text = "START",
    width = 17,
    height = 2,
    bg = "light Grey",
    fg = "black",
    )
OnOffButton.config(command=ButtonCommand)

OnOffButton.pack(pady=50)
MainWindow.mainloop()
