from tkinter import *
from tkinter import messagebox
import code

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def answer():
    if is_int(hn.get()) and is_int(mn.get()) and is_int(hk.get()) and is_int(mk.get()):
        lab['text'] = code.check(int(hn.get()), int(mn.get()), int(hk.get()), int(mk.get()))
    else:
        messagebox.showerror('Ошибка', 'Некорректный ввод')
root = Tk()
root['bg'] = '#ff7c5c'
root.title('Часы с боем')
root.geometry('315x120')
root.resizable(width=False, height=False)
hn = Entry(root, width=15, relief = FLAT, bg = '#ffe8e3', font = ("Consolas", 12, "bold"), fg = '#330a00')
mn = Entry(root, width=15, relief = FLAT, bg = '#ffe8e3', font = ("Consolas", 12, "bold"), fg = '#330a00')
hk = Entry(root, width=15, relief = FLAT, bg = '#ffe8e3', font = ("Consolas", 12, "bold"), fg = '#330a00')
mk = Entry(root, width=15, relief = FLAT, bg = '#ffe8e3', font = ("Consolas", 12, "bold"), fg = '#330a00')
but = Button(root, width=15, relief = FLAT, text = 'Узнать', bg = '#ffa994', font = ("Consolas", 12, "bold"), fg = '#330a00', command = answer)
lab = Label(root, width=10, text = '', bg = '#ffa994', font = ("Consolas", 12, "bold"), fg = '#330a00')
hn.place(x = 15, y = 15)
mn.place(x = 160, y = 15)
hk.place(x = 15, y = 45)
mk.place(x = 160, y = 45)
but.place(x = 15, y = 75)
lab.place(x = 170, y = 75)
root.mainloop()
