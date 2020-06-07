from tkinter import *
from tkinter import ttk 

class MainGUI():
    def __init__(self, master):
        # Init for main window
        self.master = master
        master.title("Calculator")

        self.saved_val = 0
        self.curr_op = ""
        self.curr_val = 0
        self.result = 0
    
        # Main interface starts here
        ''' Row 1 '''
        self.lb1 = Label(master, text="")

        ''' Row 2 '''
        self.reset_btn = Button(master, text="AC", width=5, height=2, command=lambda: self.clear_window())
        self.percent_btn = Button(master, text="%", width=5, height=2, command=lambda: self.percent())
        self.back_btn = Button(master, text="⬅︎", width=5, height=2, command=lambda: self.back())
        self.div_btn = Button(master, text="÷", width=5, height=2, command=lambda: self.division())

        ''' Row 3 '''
        self.seven = Button(master, text="7", width=5, height=2, command=lambda: self.btn_press(7))
        self.eight = Button(master, text="8", width=5, height=2, command=lambda: self.btn_press(8))
        self.nine = Button(master, text="9", width=5, height=2, command=lambda: self.btn_press(9))
        self.mult_btn = Button(master, text="×", width=5, height=2, command=lambda: self.multiplication())

        ''' Row 4 '''
        self.four = Button(master, text="4", width=5, height=2, command=lambda: self.btn_press(4))
        self.five = Button(master, text="5", width=5, height=2, command=lambda: self.btn_press(5))
        self.six = Button(master, text="6", width=5, height=2, command=lambda: self.btn_press(6))
        self.sub_btn = Button(master, text="−", width= 5, height=2, command=lambda: self.subtraction())

        ''' Row 5 '''
        self.one = Button(master, text="1", width=5, height=2, command=lambda: self.btn_press(1))
        self.two = Button(master, text="2", width=5, height=2, command=lambda: self.btn_press(2))
        self.three = Button(master, text="3", width=5, height=2, command=lambda: self.btn_press(3))
        self.add_btn = Button(master, text="+", width=5, height=2, command=lambda: self.addition())

        ''' Row 6 '''
        self.zero = Button(master, text="0", width=11, height=2, command=lambda: self.btn_press(0))
        self.dec_btn = Button(master, text=".", width=5, height=2, command=lambda: self.comma())
        self.eq_btn = Button(master, text="=", width=5, height=2, command=lambda: self.eq_func())

        # Aligns using grid
        self.lb1.grid(row=0, column=0, columnspan=4)
        self.reset_btn.grid(row=1, column=0)
        self.percent_btn.grid(row=1, column=1)
        self.back_btn.grid(row=1, column=2)
        self.div_btn.grid(row=1, column=3)
        self.seven.grid(row=2, column=0)
        self.eight.grid(row=2, column=1)
        self.nine.grid(row=2, column=2)
        self.mult_btn.grid(row=2, column=3)
        self.four.grid(row=3, column=0)
        self.five.grid(row=3, column=1)
        self.six.grid(row=3, column=2)
        self.sub_btn.grid(row=3, column=3)
        self.one.grid(row=4, column=0)
        self.two.grid(row=4, column=1)
        self.three.grid(row=4, column=2)
        self.add_btn.grid(row=4, column=3)
        self.zero.grid(row=5, column=0, columnspan=2)
        self.dec_btn.grid(row=5, column=2)
        self.eq_btn.grid(row=5, column=3)

    # Methods
    def clear_window(self):
        self.lb1["text"] = ""
        self.saved_val = 0

    def btn_press(self, num):
        if len(self.lb1["text"]) >= 9:
            return False
        else:
            self.lb1["text"] += "{}".format(num)

    def addition(self):
        if len(self.lb1["text"]) == 0:
            return False
        else:
            self.saved_val = float(self.lb1["text"])
            self.curr_op = "add"
            self.lb1["text"] = ""

    def back(self):
        if len(self.lb1["text"]) == 0:
            return False
        else:
            self.lb1["text"] = self.lb1["text"][:- 1]

    def subtraction(self):
        if len(self.lb1["text"]) == 0:
            return False
        else:
            self.saved_val = float(self.lb1["text"])
            self.curr_op = "sub"
            self.lb1["text"] = ""

    def multiplication(self):
        if len(self.lb1["text"]) == 0:
            return False
        else:
            self.saved_val = float(self.lb1["text"])
            self.curr_op = "mult"
            self.lb1["text"] = ""

    def division(self):
        if len(self.lb1["text"]) == 0:
            return False
        else:
            self.saved_val = float(self.lb1["text"])
            self.curr_op = "div"
            self.lb1["text"] = ""

    def eq_func(self):
        self.curr_val = float(self.lb1["text"])

        if self.curr_op == "add":
            self.result = self.saved_val + self.curr_val
        elif self.curr_op == "sub":
            self.result = self.saved_val - self.curr_val
        elif self.curr_op == "mult":
            self.result = self.saved_val * self.curr_val
        elif self.curr_op == "div":
            if float(self.lb1["text"]) == 0:
                self.lb1["text"] = "Error, can't divide by zero"
                return False
            else:
                self.result = self.saved_val / self.curr_val

        self.lb1["text"] = str(self.result)

    def comma(self):
        if len(self.lb1["text"]) == 0:
            return False
        else:
            self.lb1["text"] += "."

    def percent(self):
        self.lb1["text"] = "{}%".format(float(self.lb1["text"])*100)


# Runs tkinter
root = Tk()
calc_gui = MainGUI(root)
root.mainloop()