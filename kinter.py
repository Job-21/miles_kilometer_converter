from tkinter import *
window = Tk()
window.geometry("700x500")

label1 = Label(text="LOGIN", font=("Arial", 24, "bold"))
label1.pack()

def click():
    label1.config(text="SIGN UP")

btn = Button(text="CLICK ME", command=click)
btn.pack()

window.mainloop()