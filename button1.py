from tkinter import*
root=Tk()
root.title("demo")
root.geometry("500x300+500+300")
root.config(bg="red")
b1=Button(text="first",width=20)
b1.pack(pady=20)
b2=Button(text="second",width=20)
b2.pack(pady=20)
b3=Button(text="third",width=20)
b3.pack(pady=20)

mainloop()