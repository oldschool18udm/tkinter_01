import tkinter as tk


def light():
    colors = ['#F0F8FF', '#F8F8FF', '#696969']
    window.config(background=colors[0])
    lab.config(background=colors[0], foreground=colors[-1])
    btn1.config(background=colors[1], foreground=colors[-1])
    btn2.config(background=colors[1], foreground=colors[-1])


def dark():
    colors = ['#696969', '#708090', '#F0FFFF']
    window.config(background=colors[0])
    lab.config(background=colors[0], foreground=colors[-1])
    btn1.config(background=colors[1], foreground=colors[-1])
    btn2.config(background=colors[1], foreground=colors[-1])


myfont = ('Arial', 25, 'normal')
window = tk.Tk()
window.geometry('300x400')

lab = tk.Label(text='☯', font=('Arial', 55, 'normal'))
lab.pack()
btn1 = tk.Button(text='Светлая тема', font=myfont, command=light, width=13)
btn1.pack()

btn2 = tk.Button(text='Темная тема', font=myfont, command=dark, width=13)
btn2.pack()
light()
window.mainloop()
