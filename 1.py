from tkinter import * 
def body(): 
    label.config(text = "")
    lebel1.config(text = "")
    lebel2.config (text = "")
    if var.get()== 1:
        lebel.config(text = "Красный", fg = "red")
    if var.get() == 2:
        label1.config(text = "Желтый", fg = "yellow")
    if var.get() == 3:
        label2.config(text = "Зелёный", fg = "green")
root = Tk()
root.geometry("200x153")
root.resizable(width = True, height = True)
root.config(bg = "lavender")
var = IntVar()
rb1 = Radiobutton(text = "     \n    ",bg = "red",variable = var, value = 1, command = body)
rb1.pack(anchor = W)
rb2 = Radiobutton(text = "     \n    ",bg = "yellow",variable = var, value = 2, command = body)
rb.pack2(anchor = W)
rb3 = Radiobutton(text = "     \n    ",bg = "green",variable = var, value = 3, command = body)
rb3.pack(anchor = W)

label = Label(root, bg = "lavender",font = "Times 14")
lebel.place(x = 120, y = 20, anchor = CENTER)
label1 = Label(root, bg = "lavendr", font = "Times 14")
label1.place(x = 120, y = 50, anchor = CENTER)
label2 = Label(root, bg = "lavendr" ,font = "Times 14")
lebel2.place(x = 120, y = 90, anchor = CENTER)
root.mainloop()
