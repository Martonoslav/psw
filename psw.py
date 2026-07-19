import random
from tkinter import *

root = Tk()
root.geometry("1000x600")
root.title("Password generator")
root.resizable(False, False)

l = False
u = False
n = False
s = False
c = False
customsymbols = ''
symbols = []

def Appending():
    global symbols, customsymbols
    symbols = []
    if l:
        symbols.append(lowercase)
    if u:
        symbols.append(uppercase)
    if n:
        symbols.append(numbers)
    if s:
        symbols.append(special)
    if c and customsymbols:
        symbols.append(customsymbols)
    symbols = ''.join(symbols)

    output.delete(1.0, END)
    for _ in range(10):
        try:
            a = []
            for _ in range(int(variable_or_sum.get())):
                b = random.choice(symbols)
                a.append(b)
            output.insert(END, ''.join(a) + '\n')
        except IndexError as e:
            output.delete(1.0, END)
            output.insert(END, str(e))

def SetFalse(value):
    global l, u, n, s
    if value == 'l':
        l = not l
    elif value == 'u':
        u = not u
    elif value == 'n':
        n = not n
    elif value == 's':
        s = not s
    Appending()

def Customs():
    global c, customsymbols
    c = not c
    if c:
        questionw = Toplevel()
        questionw.geometry("300x200")
        questionw.title("Custom characters")
        questionw.resizable(True, False)

        l1 = Label(questionw, text='Input characters that you want to include, e.g. "$=+-<"')
        l1.pack()
        customsymbols_entry = Entry(questionw)
        customsymbols_entry.pack()

        def gh():
            global customsymbols
            customsymbols = customsymbols_entry.get()
            Appending()

        btn1 = Button(questionw, text="Enter", command=gh)
        btn1.pack()
        

lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special = '!#$%&()*+,-./:;<=>?@[]^_{|}~'

Checkbutton1 = IntVar()
Button1 = Checkbutton(root, text="Lowercase",
                    variable=Checkbutton1,
                    onvalue=1,
                    offvalue=0,
                    height=2,
                    width=10,
                    command=lambda: SetFalse('l'))
Button1.pack()

Checkbutton2 = IntVar()
Button2 = Checkbutton(root, text="Uppercase",
                    variable=Checkbutton2,
                    onvalue=1,
                    offvalue=0,
                    height=2,
                    width=10,
                    command=lambda: SetFalse('u'))
Button2.pack()

Checkbutton3 = IntVar()
Button3 = Checkbutton(root, text="Numbers",
                    variable=Checkbutton3,
                    onvalue=1,
                    offvalue=0,
                    height=2,
                    width=10,
                    command=lambda: SetFalse('n'))
Button3.pack()

Checkbutton4 = IntVar()
Button4 = Checkbutton(root, text="Special",
                    variable=Checkbutton4,
                    onvalue=1,
                    offvalue=0,
                    height=2,
                    width=10,
                    command=lambda: SetFalse('s'))
Button4.pack()

Checkbutton5 = IntVar()
Button5 = Checkbutton(root, text="Custom",
                    variable=Checkbutton5,
                    onvalue=1,
                    offvalue=0,
                    height=2,
                    width=10,
                    command=lambda: Customs())
Button5.pack()

variable_or_sum = IntVar()
l3 = Label(root, text="Password length")
l3.pack()

scl = Scale(root, variable=variable_or_sum, orient='horizontal', from_=1, to=80, command=lambda _: Appending())
scl.pack()

btn = Button(root, text="Reroll", command=lambda: Appending())
btn.pack()

output = Text(root)
output.pack()

root.mainloop()