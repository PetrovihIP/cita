from tkinter import *
import math

class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 25, "bold"), bg="#000", foreground="#FFF")
        self.lbl.place(x=12, y=40)

        btns = [
            "C", "DEL", "X^2", "1",
            "2", "3", "4", "5",
            "6", "7", "8", "9",
            "0", "*", "/", "-",
            "(", "0", ")", "%", "="
        ]

        x = 12
        y = 100
        for bt in btns:
            com = lambda x=bt: self.logica(x)
            Button(text=bt, bg="#FFF",
                   font=("Times New Roman", 12),
                   command=com).place(x=x, y=y,
                                      width=100,
                                      height=40)
            x += 110
            if x > 300:
                x = 12
                y += 60

    def logica(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "L":
            self.formula = str((eval(self.formula))%10)
        elif operation == "√":
            self.formula = str(math.sqrt(eval(self.formula)))
        elif operation == "X^2":
            self.formula = str((eval(self.formula))**2)
        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("350x510")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
