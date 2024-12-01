import tkinter as tk


def push():
    mass = float(ent_mass.get())
    height = float(ent_height.get())
    imt = mass / (0.01*height) ** 2
    if imt < 18.5:
        res = "Недостаток веса"
        color = "yellow"
    elif imt < 25:
        res = "Нормальный вес"
        color = "green"
    elif imt < 30:
        res = "Избыточный вес"
        color = 'orange'
    else:
        res = "Ожирение"
        color = "red"
    lab_result.config(text=res, foreground=color)


myfont = ('Arial', 25, 'normal')
window = tk.Tk()
window.geometry('400x400')

lab_mass = tk.Label(text='Масса тела:', font=myfont)
ent_mass = tk.Entry(font=myfont)
lab_height = tk.Label(text='Рост в см:', font=myfont)
ent_height = tk.Entry(font=myfont)
btn = tk.Button(text='Определить', font=myfont, command=push)
lab_result = tk.Label(font=myfont, text='*')
lab_mass.pack()
ent_mass.pack()
lab_height.pack()
ent_height.pack()
btn.pack()
lab_result.pack()

window.mainloop()
