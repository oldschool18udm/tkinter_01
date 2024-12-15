import random
import tkinter as tk


def add_items_to_order():
    order = []
    for i in range(len(stars)):
        if dv.get() == i:
            order.append(stars[i])
    for i in range(len(balls)):
        if fv[i].get():
            order.append(balls[i])
    print(order)
    return order


def make_order():
    global tree, stars_img, balls_img, stars
    order = add_items_to_order()
    order_window = tk.Toplevel()
    order_window.geometry('700x900')
    canv = tk.Canvas(background='white', master=order_window, width=700, height=900)
    canv.place(x=0, y=50)
    canv.create_image(700 // 2, 900 // 2, image=tree)

    # lab = tk.Label(master=order_window, font=myfont, image=tree, compound=tk.BOTTOM)
    # txt = "Вы заказали :\n" + ', '.join(order)
    # lab.config(text=txt)
    # lab.place(x=0, y=0)

    for elem in stars:
        if order[0] == elem:
            k = stars.index(elem)
            print(elem, k)
            star = stars_img[k]
            print(star)
            canv.create_image(350, 100, image=star)
            # tk.Label(image=star, master=order_window).place(x=280,y=75)
    for i in range(1, len(order)):
        for elem in balls:
            if order[i] == elem:
                k = balls.index(elem)
                bb = balls_img[k]
                canv.create_image(random.randint(0, 500), random.randint(0, 800), image=bb)


window = tk.Tk()
window.geometry('1200x600+30+30')
window.title('******')

myfont = ('Arial', 15, 'normal')

tree = tk.PhotoImage(file='./img_xmas/tree_01.png')
stars = ['Звезда 1', 'Звезда 2', 'Звезда 3', 'Звезда 4']
stars_img = [tk.PhotoImage(file='./img_xmas/star01_01.png'), tk.PhotoImage(file='./img_xmas/star02_01.png'),
             tk.PhotoImage(file='./img_xmas/star03_01.png'), tk.PhotoImage(file='./img_xmas/star04_01.png')]

balls = ['Синий', 'Золотой', 'Зеленый', 'Красный']
balls_img = [tk.PhotoImage(file='./img_xmas/blue_01.png'), tk.PhotoImage(file='./img_xmas/gold_01.png'),
             tk.PhotoImage(file='./img_xmas/green_01.png'), tk.PhotoImage(file='./img_xmas/red_01.png')]
# logo_img = tk.PhotoImage(file='./img/logo.png')

logo_lab = tk.Label(master=window, text='Добро пожаловать севис подбора елочных украшений',
                    font=myfont,
                    compound=tk.RIGHT)
logo_lab.place(x=0, y=0)

dv = tk.IntVar()
dv.set(-1)
d = []
for i in range(len(stars)):
    d.append(tk.Radiobutton(text=stars[i], variable=dv, value=i,
                            image=stars_img[i], compound=tk.TOP, command=add_items_to_order, font=myfont))
    d[-1].place(x=i * 300, y=100)

fv = [tk.BooleanVar() for elem in balls]
f = []
for i in range(len(balls)):
    f.append(tk.Checkbutton(text=balls[i], variable=fv[i], onvalue=1, offvalue=0, image=balls_img[i], compound=tk.TOP,
                            command=add_items_to_order, font=myfont))
    f[-1].place(x=i * 300, y=300)

btn_order = tk.Button(text='Посмотреть дизайн', command=make_order, font=myfont)
btn_order.place(x=600, y=500)
window.mainloop()
