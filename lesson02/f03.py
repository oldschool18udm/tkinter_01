import tkinter as tk


def summ():
    num1 = float(ent_num1.get())
    num2 = float(ent_num2.get())
    lab_res.config(text=f'Сумма: {num1 + num2}')


def difference():
    num1 = float(ent_num1.get())
    num2 = float(ent_num2.get())
    lab_res.config(text=f'Разность: {num1 - num2}')


def multiplication():
    num1 = float(ent_num1.get())
    num2 = float(ent_num2.get())
    lab_res.config(text=f'Произведение: {num1 * num2}')


def division():
    num1 = float(ent_num1.get())
    num2 = float(ent_num2.get())
    if num2 == 0:
        lab_res.config(text='Error')
    else:
        lab_res.config(text=f'Частное:{num1 / num2}')


myfont = ('Arial', 20, 'normal')
window = tk.Tk()
window.geometry('400x400')

lab_res = tk.Label(font=myfont)

ent_num1 = tk.Entry(font=myfont)
ent_num2 = tk.Entry(font=myfont)

btn_sum = tk.Button(width=4, font=myfont, text='+', command=summ)
btn_diff = tk.Button(width=4, font=myfont, text='-', command=difference)
btn_mult = tk.Button(width=4, font=myfont, text='*', command=multiplication)
btn_div = tk.Button(width=4, font=myfont, text='/', command=division)

ent_num1.pack()
ent_num2.pack()
btn_sum.pack()
btn_diff.pack()
btn_mult.pack()
btn_div.pack()

lab_res.pack()

window.mainloop()
