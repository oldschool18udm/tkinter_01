import tkinter as tk


def push():
    animals='обезьяны петуха собаки свиньи крысы быка тигра кролика дракона змеи лошадии козы'.split()
    num = int(ent_year.get())
    res = animals[num%12]
    lab_animal.config(text=f'{num} - год {res}')


myfont = ('Arial', 25, 'normal')
window = tk.Tk()
window.geometry('400x400')
ent_year = tk.Entry(font=myfont)
btn = tk.Button(text='Определить',font=myfont, command=push)
lab_animal = tk.Label(font=myfont)

ent_year.pack()
btn.pack()
lab_animal.pack()

window.mainloop()
