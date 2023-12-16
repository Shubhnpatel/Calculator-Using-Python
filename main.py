import tkinter
from tkinter import *

def button_click(number):
    current = label_result.cget("text")
    label_result.config(text=current + str(number))

def button_clear():
    label_result.config(text="")

def button_equal():
    try:
        current = label_result.cget("text")
        result = eval(current)
        label_result.config(text=str(result))
    except Exception as e:
        label_result.config(text="Error")

root = Tk()
root.title("Simple calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="#17161b")

label_result = Label(root, width=20, height=2, text="", font=("arial", 30))
label_result.pack()

# Buttons
Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5",
       command=button_clear).place(x=10, y=100)

Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: button_click("/")).place(x=150, y=100)

Button(root, text="%", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: button_click("%")).place(x=290, y=100)

Button(root, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: button_click("*")).place(x=430, y=100)

Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: button_click(7)).place(x=10, y=200)

Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: button_click(8)).place(x=150, y=200)

Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: button_click(9)).place(x=290, y=200)

Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: button_click("+")).place(x=430, y=200)

Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: button_click(4)).place(x=10, y=300)

Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: button_click(5)).place(x=150, y=300)

Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: button_click(6)).place(x=290, y=300)

Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: button_click("-")).place(x=430, y=300)

Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: button_click(1)).place(x=10, y=400)

Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: button_click(2)).place(x=150, y=400)

Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: button_click(3)).place(x=290, y=400)

Button(root, text="=", width=5, height=3, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="orange",
       command=button_equal).place(x=430, y=400)

Button(root, text="0", width=11, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: button_click(0)).place(x=10, y=500)

Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: button_click(".")).place(x=290, y=500)

root.mainloop()
