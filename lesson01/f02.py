import tkinter as tk
import random


def push():
    lab_number.config(text=random.randint(1, 20))
    colors = ['#6495ED', '#DE3163', '#9FE2BF', '#CCCCFF', '#FFBF00']
    btn1.config(background=random.choice(colors))


def foo():
    hello = ['Привет', 'Добрый день', 'Доброе утро', 'Добрый вечер', 'Здравствуйте']
    lab_hello.config(text=random.choice(hello))


myfont = ('Arial', 25, 'italic')
window = tk.Tk()
window.geometry('300x400')

lab_number = tk.Label(text='1', font=myfont)
lab_number.pack()
btn1 = tk.Button(text='Нажми', font=myfont, command=push)
btn1.pack()

lab_hello = tk.Label(text='Hello', font=myfont)
lab_hello.pack()
btn2 = tk.Button(text='Нажми', font=myfont, command=foo)
btn2.pack()

window.mainloop()
