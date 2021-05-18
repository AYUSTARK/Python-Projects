from tkinter import *


# noinspection PyAttributeOutsideInit
class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.task = ""
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.user_input = Entry(self, bg="#5BC8AC", bd=29, insertwidth=4, width=24, font=("Verdana", 20, "bold"),
                                textvariable=self.UserIn, justify=RIGHT)
        self.user_input.grid(columnspan=4)

        self.user_input.insert(0, "0")
        self.button1 = Button(self, bg="#98DBC6", bd=12, text="7", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(7))
        self.button1.grid(row=2, column=0, sticky=W)

        self.button2 = Button(self, bg="#98DBC6", bd=12, text="8", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(8))
        self.button2.grid(row=2, column=1, sticky=W)

        self.button3 = Button(self, bg="#98DBC6", bd=12, text="9", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(9))
        self.button3.grid(row=2, column=2, sticky=W)

        self.button4 = Button(self, bg="#98DBC6", bd=12, text="4", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(4))
        self.button4.grid(row=3, column=0, sticky=W)

        self.button5 = Button(self, bg="#98DBC6", bd=12, text="5", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(5))
        self.button5.grid(row=3, column=1, sticky=W)

        self.button6 = Button(self, bg="#98DBC6", bd=12, text="6", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(6))
        self.button6.grid(row=3, column=2, sticky=W)

        self.button7 = Button(self, bg="#98DBC6", bd=12, text="1", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(1))
        self.button7.grid(row=4, column=0, sticky=W)

        self.button8 = Button(self, bg="#98DBC6", bd=12, text="2", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(2))
        self.button8.grid(row=4, column=1, sticky=W)

        self.button9 = Button(self, bg="#98DBC6", bd=12, text="3", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(3))
        self.button9.grid(row=4, column=2, sticky=W)

        self.button0 = Button(self, bg="#98DBC6", bd=12, text="0", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(0))
        self.button0.grid(row=5, column=0, sticky=W)

        self.buttonAdd = Button(self, bg="#98DBC6", bd=12, text="+", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                                command=lambda: self.buttonClick("+"))
        self.buttonAdd.grid(row=2, column=3, sticky=W)

        self.buttonSub = Button(self, bg="#98DBC6", bd=12, text="-", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                                command=lambda: self.buttonClick("-"))
        self.buttonSub.grid(row=3, column=3, sticky=W)

        self.buttonMulti = Button(self, bg="#98DBC6", bd=12, text="X", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                                  command=lambda: self.buttonClick("*"))
        self.buttonMulti.grid(row=4, column=3, sticky=W)

        self.buttonDiv = Button(self, bg="#98DBC6", bd=12, text="/", padx=33, pady=25, font="Helvetica 20 bold",
                                command=lambda: self.buttonClick("/"))
        self.buttonDiv.grid(row=5, column=3, sticky=W)

        self.buttonEqual = Button(self, bg="#98DBC6", bd=12, text="=", padx=100, pady=25,
                                  font=("Helvetica", 20, "bold"),
                                  command=lambda: self.calculate())
        self.buttonEqual.grid(row=5, column=1, sticky=W, columnspan=2)

        self.buttonClear = Button(self, bg="#98DBC6", bd=12, text="AC", padx=33, pady=15,
                                  font=("Helvetica", 20, "bold"), command=lambda: self.clearDisplay())
        self.buttonClear.grid(row=1, columnspan=4, sticky=W)

    def buttonClick(self, num):
        self.task = str(self.task) + str(num)
        self.UserIn.set(self.task)
        pass

    def clearDisplay(self):
        self.task = ""
        self.UserIn.set(self.task)
        pass

    def calculate(self):
        self.data = self.user_input.get()
        try:
            self.answer = eval(self.data)
            self.displayText(self.answer)
            self.task = str(self.answer)
        except SyntaxError as s:
            self.displayText("Invalid Input")
            self.task = ''
        pass

    def displayText(self, answer):
        self.UserIn.set(answer)
        pass


if __name__ == '__main__':
    calculator = Tk()
    calculator.title("Calculator")
    Application(calculator)
    calculator.resizable(width=False, height=False)
    calculator.mainloop()
