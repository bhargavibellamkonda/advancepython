from tkinter import*
root=Tk()
root.title("demo")
root.geometry("500x300+500+300")
root.config(bg="red")
lb1=Label(text="Welcome to Tkinter",bg="yellow",fg="cyan",font=("verdana",20,"bold"))
lb1.pack(pady=20)
mainloop()