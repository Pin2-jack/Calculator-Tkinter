# Program to perform basic Calculator functions
from tkinter import *
root = Tk()
root.title("Calculator!")

heading = Entry(root, width=40, borderwidth=5)
heading.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
heading.insert(0, " ")

def button_click(number):
    current = heading.get()
    heading.delete(0, END)
    heading.insert(0, str(current) + str(number))

def button_add():
    first_num = heading.get()
    global first_number
    global action
    action = "addition"
    first_number = int(first_num)
    heading.delete(0, END)

def button_substract():
    first_num = heading.get()
    global first_number
    global action
    action = "substraction"
    first_number = int(first_num)
    heading.delete(0, END)

def button_multiply():
    first_num = heading.get()
    global first_number
    global action
    action = "multiplication"
    first_number = int(first_num)
    heading.delete(0, END)

def button_equal():
    second_num = heading.get()
    heading.delete(0, END)
    if action == "addition":
        heading.insert(0, first_number + int(second_num))
    if action == "substraction":
        heading.insert(0, first_number - int(second_num))
    if action == "multiplication":
        heading.insert(0, first_number * int(second_num))

def button_clear():
    heading.delete(0, END)



Button1 = Button(root, text="1", padx=40, pady=20, command=lambda:button_click(1))
Button2 = Button(root, text="2", padx=40, pady=20, command=lambda:button_click(2))
Button3 = Button(root, text="3", padx=40, pady=20, command=lambda:button_click(3))
Button4 = Button(root, text="4", padx=40, pady=20, command=lambda:button_click(4))
Button5 = Button(root, text="5", padx=40, pady=20, command=lambda:button_click(5))
Button6 = Button(root, text="6", padx=40, pady=20, command=lambda:button_click(6))
Button7 = Button(root, text="7", padx=40, pady=20, command=lambda:button_click(7))
Button8 = Button(root, text="8", padx=40, pady=20, command=lambda:button_click(8))
Button9 = Button(root, text="9", padx=40, pady=20, command=lambda:button_click(9))
Button0 = Button(root, text="0", padx=40, pady=20, command=lambda:button_click(0))

Button_add = Button(root, text="+", padx=38, pady=20, command=button_add)
Button_substract = Button(root, text="-", padx=40, pady=20, command=button_substract)
Button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
Button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal)
Button_clear = Button(root, text="clear", padx=30, pady=20, command=button_clear)

Button1.grid(row=1,column=0)
Button2.grid(row=1,column=1)
Button3.grid(row=1,column=2)
Button4.grid(row=2,column=0)
Button5.grid(row=2,column=1)
Button6.grid(row=2,column=2)
Button7.grid(row=3,column=0)
Button8.grid(row=3,column=1)
Button9.grid(row=3,column=2)
Button0.grid(row=4,column=0)
Button_add.grid(row=4,column=1)
Button_substract.grid(row=4,column=2)
Button_multiply.grid(row=5,column=1)
Button_equal.grid(row=5,column=2)
Button_clear.grid(row=5,column=0)

#Button1.pack()

#Button1.grid(row=1, column=0)

root.mainloop()