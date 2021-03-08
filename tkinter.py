import tkinter
from tkinter import ttk

root = tkinter.Tk()
label = tkinter.Label(root, text="Hello World!")
label.pack()
button1 = tkinter.Button(root, text = 'Button1').pack()
button2 = ttk.Button(root, text = 'Button2').pack()
root.mainloop()
