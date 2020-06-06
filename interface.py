from tkinter import *
from tkinter import ttk 
import functions as func


class MainGUI():
    def __init__(self, master):
        # Init for main window
        self.master = master
        master.title("Calculator")

        # Main interface starts here
        ''' Row 1 '''
        self.lb1 = Label(master, text="0")

        ''' Row 2 '''
        self.reset_btn = Button(master, text="AC", width=5, height=2)
        self.pm_btn = Button(master, text="+/-", width=5, height=2)
        self.percent_btn = Button(master, text="%", width=5, height=2)
        self.div_btn = Button(master, text="/", width=5, height=2)

        ''' Row 3 '''
        self.seven = Button(master, text="7", width=5, height=2)
        self.eight = Button(master, text="8", width=5, height=2)
        self.nine = Button(master, text="9", width=5, height=2)
        self.mult_btn = Button(master, text="*", width=5, height=2)

        ''' Row 4 '''
        self.four = Button(master, text="4", width=5, height=2)
        self.five = Button(master, text="5", width=5, height=2)
        self.six = Button(master, text="6", width=5, height=2)
        self.sub_btn = Button(master, text="-", width= 5, height=2)

        ''' Row 5 '''
        self.one = Button(master, text="1", width=5, height=2, command=lambda: self.btn_press(1))
        self.two = Button(master, text="2", width=5, height=2)
        self.three = Button(master, text="3", width=5, height=2)
        self.plus_btn = Button(master, text="+", width=5, height=2)

        ''' Row 6 '''
        self.zero = Button(master, text="0", width=11, height=2)
        self.dec_btn = Button(master, text=",", width=5, height=2)
        self.eq_btn = Button(master, text="=", width=5, height=2)

        # Aligns with grid
        self.lb1.grid(row=0, column=0, columnspan=4)
        self.reset_btn.grid(row=1, column=0)
        self.pm_btn.grid(row=1, column=1)
        self.percent_btn.grid(row=1, column=2)
        self.div_btn.grid(row=1, column=3)
        self.seven.grid(row=2, column=0)
        self.eight.grid(row=2, column=1)
        self.nine.grid(row=2, column=2)
        self.mult_btn.grid(row=2, column=3)
        self.four.grid(row=3, column=0)
        self.four.grid(row=3, column=1)
        self.six.grid(row=3, column=2)
        self.sub_btn.grid(row=3, column=3)
        self.one.grid(row=4, column=0)
        self.two.grid(row=4, column=1)
        self.three.grid(row=4, column=2)
        self.plus_btn.grid(row=4, column=3)
        self.zero.grid(row=5, column=0, columnspan=2)
        self.dec_btn.grid(row=5, column=2)
        self.eq_btn.grid(row=5, column=3)

    # Methods
    def btn_press(self, num):
        self.lb1["text"] += "{}".format(num)


# Runs tkinter
root = Tk()
calc_gui = MainGUI(root)
root.mainloop()