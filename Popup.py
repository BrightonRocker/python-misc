import tkinter as tk

def popupmsg(msg):
    root = tk.Tk()
    label = tk.Label(root, text=msg)
    label.pack(side="top", fill="y", pady=100)
    B1 = tk.Button(root, text=Txt1, command = root.destroy)
    B1.pack()

    
msg = "HIII"
Txt1 = "Press me to close :("
popupmsg(msg)
msg = "Don't worry I haven't hacked you!"
popupmsg(msg)
msg = "I just wanted to say hi"
popupmsg(msg)
msg = "After all this time I finally figured out how to make pop ups in python"
popupmsg(msg)
msg = "And I only had to use tkinter!"
popupmsg(msg)
