import tkinter as tk
import time

def motion():
    value = a.get()
    if value == 1:
        label.config(text = "Тормозим", font = "Arial 15", anchor = "center", fg = "black", bg = "red")
    elif value == 2:
        label.config(text = "скоро начнем движение", font = "Arial 15", anchor="center", fg = "black", bg = "yellow")
    elif value == 3:
        label.config(text = "Вперед", font = "Arial 15", anchor = "center", fg = "black", bg = "green")
        for i in range(100):
            canvas.move(cr, 0, -7)
            root.update()
            time.sleep(0.1)

    value = b.get()
    if value == 4:
        label.config(text = "СТОП", font = "Arial 15", anchor = "center", fg = "black", bg = "red")
    elif value == 5:
        label.config(text = "Скоро поедем", font = "Arial 15", anchor = "center", fg = "black", bg = "yellow")
    elif value == 6:
        label.config(text = "Зелёный ура!", font = "Arial 15", anchor = "center", fg = "black", bg = "green")
        for i in range(100):
            canvas.move(dr, 7, 0)
            root.update()
            time.sleep(0.1)

root = tk.Tk()
root.title("на перекрестке")
root.resizable(False, False)

road = tk.PhotoImage(file = "road.png")
canvas = tk.Canvas(root, width = 650, height = 500)
canvas.create_image(0, 0, anchor = "nw", image = road)
canvas.pack()

tachka = tk.PhotoImage(file = "tachka.png")
cr = canvas.create_image(360, 380, anchor = "nw", image = tachka)

tachka1 = tk.PhotoImage(file = "tachka1.png")
dr = canvas.create_image(15, 265, anchor = "nw", image = tachka1)

a = tk.IntVar()

frame_bottom = tk.Frame(root, bd = 2, bg = "black")
frame_bottom.place(x = 525, y = 300)
rb1 = tk.Radiobutton(frame_bottom, variable = a, value = 1, bg = "red", fg = "red", width = 3, height = 3, command = motion)
rb1.pack()
rb2 = tk.Radiobutton(frame_bottom, variable = a, value = 2, bg = "yellow", fg = "yellow", width = 3, height = 3, command = motion)
rb2.pack()
rb3 = tk.Radiobutton(frame_bottom, variable = a, value = 3, bg = "green", fg = "green", width = 3, height = 3, command = motion)
rb3.pack()

b = tk.IntVar()

frame_bottom1 = tk.Frame(root, bd = 2, bg = "black")
frame_bottom1.place(x = 70, y = 0)
rb4 = tk.Radiobutton(frame_bottom1, variable = b, value = 4, bg = "red", fg = "red", width = 3, height = 3, command = motion)
rb4.pack()
rb5 = tk.Radiobutton(frame_bottom1, variable = b, value = 5, bg = "yellow", fg = "yellow", width = 3, height = 3, command = motion)
rb5.pack()
rb6 = tk.Radiobutton(frame_bottom1, variable = b, value = 6, bg = "green", fg = "green", width = 3, height = 3, command = motion)
rb6.pack()

label = tk.Label(root, text = "...", font = "Arial 15", anchor = "center", fg = "black", bg = "gray")
label.pack(expand = True, fill = "both")

root.mainloop()
