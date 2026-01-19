from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


root = Tk()
root.title("Denomination Calculator")
root.configure(bg = "lightblue")
root.geometry("650x400")


upload = Image.open("image.jpg")

upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg = "lightblue")
label.place(x=180, y=20)

label1 = Label(root,
               text = "Hey user! Welcome to Denomination Calculator Application",
               bg = "lightblue",)
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate the den0mination count?")
    if MsgBox == "ok":
        topwin()

button1 = Button(root,
                 text="lets get started",
                 command=msg,
                bg = "brown",
                fg = "white",)
button1.place(x = 260, y = 360)


def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg = "lightgrey")
    top.geometry("600x350+50+50")


    label = Label(top, text="enter total ammount", bg = "lightgrey")
    entry = Entry(top)
    lbl = Label(top, text = "here are number of notes for each denomination", bg = "lightgrey")

    l1 = Label(top, text="2000", bg = "lightgrey")
    l2 = Label(top, texts="500", bg = "lightgrey")
    l3 = Label(top, texts="100", bg = "lightgrey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculate():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    btn = Button(top,text="Calculate", command=calculate, bg = "brown", fg = "white")


    label.place(x=230, y = 50)
    entry.place(x = 200, y = 80)
    btn.place(x = 140, y = 120)
    lbl.place(x = 140, y = 260)

    l1.place(x = 180, y = 200)
    l2.place(x = 180, y = 230)
    l3.place(x = 180, y = 260)

    t1.place(x = 270, y = 200)
    t2.place(x = 270, y = 230)
    t3.place(x = 270, y = 260)

    top.mainloop()

root.mainloop()