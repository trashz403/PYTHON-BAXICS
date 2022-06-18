from tkinter import *

window=Tk()
window.geometry("500x500")
window.title("TRASHZ403")
window.configure(bg="red")

def hello():
    print("Button clicked!")

def mangaandi():
    print("Button2 clicked!")

button1=Button(text="ok",command=hello)
button2=Button(text="ok",command=mangaandi
)

button1.grid(row=0,column=0)
button2.grid(row=0,column=1)


label=Label(window,text="Welcome")




"""button1.pack()
label.pack()"""


window.mainloop()