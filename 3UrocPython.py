# Кнопка и виджет Button

def say_привет():
    print('привет')
def abd_label():
    label= tk.Label(win,text='new')
    label.pack()
def counter():
    global count
    count+=1
    btn4['text']= f'Счетчик:{count}'
count = 0

import tkinter as tk
win = tk.Tk()
win.geometry(f"400x500+100+200")
win.title('Кнопка буттон')
photo = tk.PhotoImage(file='Da.png')
win.iconphoto(False, photo)
btn1 = tk.Button(win,text='Привет',
                 command=say_привет
                 )
btn2 = tk.Button(win,text='Abd new label',
                 command=abd_label
                 )
btn3 = tk.Button(win,text='Abd new label lambda',
                 command=lambda:tk.Label(win,text='new lambda'). pack()
                 )
btn4 = tk.Button(win,text='Счетчик: {count}',
                 command=counter,
                 activebackground='blue',
                 bg='red',
                 state=tk.NORMAL # DISABLED кнопка не работает
                 )

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()


win.mainloop()