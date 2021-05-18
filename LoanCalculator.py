from tkinter import *


class LoanCalculator:

    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")
        window.configure(background="light green")
        Label(window, font='Helvetica 12 bold', bg='light green', text='Annual Interest Rate') \
            .grid(row=1, column=1, sticky=W)

        Label(window, font='Helvetica 12 bold', bg='light green', text='Number of Years') \
            .grid(row=2, column=1, sticky=W)

        Label(window, font='Helvetica 12 bold', bg='light green', text='Loan Amount') \
            .grid(row=3, column=1, sticky=W)

        Label(window, font='Helvetica 12 bold', bg='light green', text='Monthly Payment') \
            .grid(row=4, column=1, sticky=W)

        Label(window, font='Helvetica 12 bold', bg='light green', text='Total Payment') \
            .grid(row=5, column=1, sticky=W)

        self.annualInterestRate = StringVar()
        Entry(window, textvariable=self.annualInterestRate, justify=RIGHT).grid(row=1, column=2)

        self.numberOfYears = StringVar()
        Entry(window, textvariable=self.numberOfYears, justify=RIGHT).grid(row=2, column=2)

        self.loanAmount = StringVar()
        Entry(window, textvariable=self.loanAmount, justify=RIGHT).grid(row=3, column=2)

        self.monthlyPayment = StringVar()
        Label(window, font='Helvetica 12 bold', bg='light green', fg='white', textvariable=self.monthlyPayment
              , justify=RIGHT).grid(row=4, column=2, sticky=E)

        self.totalPayment = StringVar()
        Label(window, font='Helvetica 12 bold', bg='light green', fg='white', textvariable=self.totalPayment
              , justify=RIGHT).grid(row=5, column=2, sticky=E)

        Button(window, font='Helvetica 12 bold', bg='Red', text='Compute Payment', command=lambda: self.compute()) \
            .grid(row=6, column=2, sticky=E)

        Button(window, font='Helvetica 12', bg='Blue', text='Clear', command=lambda: self.clear()) \
            .grid(row=6, column=8, padx=20, pady=20, sticky=E)

        window.mainloop()

    def compute(self):
        try:
            monthlyPayment = self.getMonthlyPayment(
                float(self.loanAmount.get()),
                float(self.annualInterestRate.get()) / 1200,
                int(self.numberOfYears.get())
            )
            self.monthlyPayment.set(format(monthlyPayment, '10.2f'))
            totalPayment = float(self.monthlyPayment.get()) * 12 * int(self.numberOfYears.get())
            self.totalPayment.set(format(totalPayment, '10.2f'))
        except ValueError:
            self.monthlyPayment.set("Invalid Input!")
            self.totalPayment.set("Invalid Input!")

    def clear(self):
        self.numberOfYears.set("")
        self.loanAmount.set("")
        self.annualInterestRate.set("")
        self.totalPayment.set("")
        self.monthlyPayment.set("")

    def getMonthlyPayment(self, loanAmount, monthlyInterest, noOfYears):
        monthlyPayment = loanAmount * monthlyInterest / (1 - 1 / (1 + monthlyInterest) ** (noOfYears * 12))
        print(
            f"{1 - 1 / (1 + monthlyInterest) ** (noOfYears * 12)} monthly {monthlyInterest} power {(1 + monthlyInterest) ** (noOfYears * 12)}")
        return monthlyPayment


if __name__ == '__main__':
    loanCalculator = LoanCalculator()
