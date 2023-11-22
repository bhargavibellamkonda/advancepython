from tkinter import *
root=Tk()
menubar=Menu()
menubar.add_command(label="File")
menubar.add_command(label="Quit")
root.config(menu=menubar)
mainloop()