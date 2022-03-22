from tkinter import *
is _on = True

def clickhere():
    global is_on 
    if is_on:
        l.config (text="Goodbye world")
        is_on = False
    else:
        l.config(text="Hello world")
        is_on = True

window = Tk()

window.title("greeting")
window.configure(background="megenta")
window.geometry("450x450")
window.realizable(True,False,)
l = Label(window,text="Hello world")
l.config(font = "impact", bg= "green", fg= "red")
l.pack()

b= Button (window, text = "Click here")
b.config(font = "Magento", bg = "blue", fg = "yellow")
b.pack()

e = Entry(width=30)

e.insert(0,"some text")
e.pack()
nameb = Button(window, text = "Enter name", command = clickhere)
b.config(font = "Magento", bg = "blue", fg ="yellow")
b.pack()

window.mainloop()