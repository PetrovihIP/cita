import tkinter as tk
win = tk.Tk()
photo = tk.PhotoImage(file='Ok.png')
win.iconphoto(False, photo)
win.config(bg='#FAFAD2')
win.title('Первая работа')
win.geometry("500x450+400+200")
win.minsize(200,300)
win.maxsize(700,600)
win.resizable(True, True)
label_1 = tk.Label(win, text='''привет всем!',
world!''',
                   bg='green', # цвет фона текста
                   fg='white', # цвет текста
                   font=('Arial',15,'bold'), # шрифт, размер, жирный
                   padx=20, # ширина
                   pady=40, # высота
                   width=20,
                   height=10,
                   anchor='s', # сторона света их 4 всего
                   relief=tk.RAISED, # граница лейбла
                   bd=20, # ширина границы
                   justify=tk.RIGHT # для подписи снизу текста

                   )

label_1.pack()


win.mainloop()
