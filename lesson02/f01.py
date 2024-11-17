import tkinter as tk


def push():
    num1 = float(ent_num1.get())
    num2 = float(ent_num2.get())
    lab_sum.config(text=f'Сумма: {num1 + num2}')
    lab_diff.config(text=f'Разность: {num1 - num2}')
    lab_mult.config(text=f'Произведение: {num1 * num2}')
    if num2 == 0:
        lab_div.config(text='Error')
    else:
        lab_div.config(text=f'Частное:{num1 / num2}')


myfont = ('Arial', 25, 'normal')
window = tk.Tk()
window.geometry('400x400')

lab_sum = tk.Label(font=myfont)
lab_diff = tk.Label(font=myfont)
lab_mult = tk.Label(font=myfont)
lab_div = tk.Label(font=myfont)

ent_num1 = tk.Entry(font=myfont)
ent_num2 = tk.Entry(font=myfont)

btn_result = tk.Button(font=myfont, text='Вычислить', command=push)

ent_num1.pack()
ent_num2.pack()

btn_result.pack()
lab_sum.pack()
lab_diff.pack()
lab_mult.pack()
lab_div.pack()
window.mainloop()
