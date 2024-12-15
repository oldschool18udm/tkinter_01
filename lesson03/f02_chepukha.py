import random
import tkinter as tk


def push():
    emo =random.choice( "радоти счастья восторга удивления".split())
    deepr = random.choice("похрюкивая мяукая погавкивая ".split())
    res = f"""Даже  {ent_animal.get()}  знает: если {ent_time.get()} повторять заклинание  "{ent_spell.get()}", 
    размахивая при этом {ent_thing2.get()}, - оно сработает! 
    И {ent_thing1.get()}, радостно {deepr}, запрыгает от {emo}, 
    а  {ent_human.get()} скажет: "{ent_wow.get()}" и побежит в магазин за  {ent_food.get()}."""
    print(res)
    lab_result.config(text=res)


myfont = ('Arial', 15, 'normal')
window = tk.Tk()
window.geometry('800x800')

lab_time = tk.Label(text='Сколько времени вы в состоянии провести без смартфона?', font=myfont)
ent_time = tk.Entry(font=myfont)

lab_animal = tk.Label(text='Какое животное вам наиболее симпатично?', font=myfont)
ent_animal = tk.Entry(font=myfont)

lab_spell = tk.Label(text='Назовите первое попавшееся заклинание из "Гарри Поттера":', font=myfont)
ent_spell = tk.Entry(font=myfont)

lab_thing1 = tk.Label(text='Какой предмет в вашем доме самый тяжёлый?', font=myfont)
ent_thing1 = tk.Entry(font=myfont)

lab_human = tk.Label(text='Кто обычно делает вам замечания?', font=myfont)
ent_human = tk.Entry(font=myfont)

lab_wow = tk.Label(text='Какими словами вы обычно выражаете крайнее удивление?', font=myfont)
ent_wow = tk.Entry(font=myfont)

lab_thing2 = tk.Label(text='Чем бы вы воспользовались, чтобы отбиться от комаров?', font=myfont)
ent_thing2 = tk.Entry(font=myfont)

lab_food = tk.Label(text='Каким продуктом питания вас можно порадовать?', font=myfont)
ent_food = tk.Entry(font=myfont)

btn = tk.Button(text='Рассказать историю', font=myfont, command=push)
lab_result = tk.Label(font=myfont, text='*')


lab_time.pack()
ent_time.pack()

lab_animal.pack()
ent_animal.pack()

lab_spell.pack()
ent_spell.pack()

lab_thing1.pack()
ent_thing1.pack()

lab_human.pack()
ent_human.pack()

lab_thing2.pack()
ent_thing2.pack()

lab_wow.pack()
ent_wow.pack()

lab_food.pack()
ent_food.pack()

lab_thing1.pack()
ent_thing1.pack()
btn.pack()
lab_result.pack()

window.mainloop()
