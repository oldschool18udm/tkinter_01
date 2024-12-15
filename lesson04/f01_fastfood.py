import tkinter as tk


def add_items_to_order():
    order = []
    for i in range(len(drinks)):
        if dv.get() == i:
            order.append(drinks[i])
    for i in range(len(food)):
        if fv[i].get():
            order.append(food[i])
    print(order)
    return order


def make_order():
    order = add_items_to_order()
    order_window = tk.Toplevel()
    order_window.geometry('250x300')
    lab = tk.Label(master=order_window, font=myfont)
    txt = "Вы заказали :\n" + '\n'.join(order)
    lab.config(text=txt)
    lab.pack()


window = tk.Tk()
window.geometry('550x900+30+30')
window.title('заказ еды')

myfont = ('Arial', 15, 'normal')
drinks = ['Кофе', 'Чай', 'Молочный коктейль']
drinks_img = [tk.PhotoImage(file='./img/coffee.png'), tk.PhotoImage(file='./img/tea.png'),
              tk.PhotoImage(file='./img/milkshake.png')]

food = ['Бургер', 'Твистер', 'Картофель фри', 'Соус']
food_img = [tk.PhotoImage(file='./img/burger.png'), tk.PhotoImage(file='./img/twister.png'),
            tk.PhotoImage(file='./img/free.png'), tk.PhotoImage(file='./img/souse.png')]
logo_img = tk.PhotoImage(file='./img/logo.png')

logo_lab = tk.Label(master=window, image=logo_img, text='Добро пожаловать в ресторан "Быстрая еда"\n Делайте Ваш заказ',
                    font=myfont,
                    compound=tk.RIGHT)
logo_lab.pack()

dv = tk.IntVar()
dv.set(-1)
d = []
for i in range(len(drinks)):
    d.append(tk.Radiobutton(text=drinks[i], variable=dv, value=i,
                            image=drinks_img[i], compound=tk.LEFT, command=add_items_to_order, font=myfont))
    d[-1].pack()

fv = [tk.BooleanVar() for elem in food]
f = []
for i in range(len(food)):
    f.append(tk.Checkbutton(text=food[i], variable=fv[i], onvalue=1, offvalue=0, image=food_img[i], compound=tk.LEFT,
                            command=add_items_to_order, font=myfont))
    f[-1].pack()

btn_order = tk.Button(text='Сделать заказ', command=make_order, font=myfont)
btn_order.pack()
window.mainloop()
