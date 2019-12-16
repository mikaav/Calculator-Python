from tkinter import *

start = True
nextcommand = "="
result = 0


def clix(text):
    global start
    global nextcommand
    global result
    if text.isdigit() or text == ".":
        if start:
            display.configure(text="")
            start = False
        if text != "." or display.cget("text").find(".") == -1:
            display.configure(text=(display.cget("text") + text))
    else:
        if start:
            nextcommand = text
        else:
            calc(float(display.cget("text")))
            nextcommand = text
            start = True


def calc(x):
    global nextcommand
    global display
    global result

    if nextcommand == "+":
        result += x
    elif nextcommand == "-":
        result -= x
    elif nextcommand == "*":
        result *= x
    elif nextcommand == "/":
        try:
            result /= x
        except ZeroDivisionError:
            result = "Error"
    elif nextcommand == "=":
        result = x
    display.configure(text=result)


root = Tk()
root.title("Python Calculator")

buttons = (("7", "8", "9", "/"),
           ("4", "5", "6", "*"),
           ("1", "2", "3", "-"),
           ("0", ".", "=", "+"))
display = Label(root, text="Calculator by Me", font="Tahoma 20", bd=20)
display.grid(row=0, column=0, columnspan=4)

for row in range(4):
    for column in range(4):
        button = Button(root, text=buttons[row][column], font="Tahoma 20",
                        command=lambda text=buttons[row][column]: clix(text))
        button.grid(row=row + 1, column=column, padx=5, pady=5, ipadx=20, ipady=20)

w = root.winfo_reqwidth()
h = root.winfo_reqheight()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = int(ws / 2 - w / 2)
y = int(hs / 4 - h / 4)
root.geometry("+{0}+{1}".format(x, y))
root.mainloop()
