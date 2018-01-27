from tkinter import *
from tkinter import messagebox
from datetime import datetime
from datetime import timedelta
import os
import time
if os.name == 'nt':
    import winsound
    import ctypes



class Timer():
    def __init__(self, master):
        self.master = master
        self.master.withdraw()
        self.master.title("Timer")
        self.master.resizable(False, False)

        self.choose_option()

        self.time_start = datetime.now()
        self.time_end = self.time_start + timedelta(hours=0.1)
        self.time_to_end_start = self.time_end - self.time_start

        self.canvas = Canvas(master)
        self.canvas.pack()
        self.canvas.config(width=300, height=300, background="black")

        self.arc = self.canvas.create_arc(10, 10, 290, 290)
        self.canvas.itemconfigure(self.arc, start = 90, extent = 270, fill = 'red4', width = 0)
        self.oval = self.canvas.create_oval(30, 30, 270, 270, fill='black')
        self.text = self.canvas.create_text(150, 150, text = '', font = ('Courier', 32, 'bold'), fill="white")
        self.update_clock()

        # self.master.deiconify()


    def choose_option(self):
        self.choose_window = Toplevel(self.master)
        self.choose_window.lift(self.master)
        self.choose_window.resizable(False, False)
        self.choose_window.grab_set()
        self.choose_window.title('Choose what to do')
        # hours spinbox
        self.hours = StringVar()
        self.hours_spinbox = Spinbox(self.choose_window, from_=0, to=100, textvariable=self.hours, width=5)
        self.hours.set("h")
        # minutes spinbox
        self.minutes = StringVar()
        self.minutes_spinbox = Spinbox(self.choose_window, from_=0, to=100, textvariable=self.minutes, width=5)
        self.minutes.set("m")
        # action_choice radio_button
        self.action_choice = IntVar()
        self.action_button_1 = Radiobutton(self.choose_window, text='lock', variable=self.action_choice, value=1)
        self.action_button_2 = Radiobutton(self.choose_window, text='shutdown', variable=self.action_choice, value=2)
        # button start
        self.start_button = Button(self.choose_window, text='START', command=self.start_countdown)



        self.hours_spinbox.grid(column=0, row=0)
        self.minutes_spinbox.grid(column=1, row=0)
        self.action_button_1.grid(column=0, columnspan=2, row=1, sticky=W)
        self.action_button_2.grid(column=0, columnspan=2, row=2, sticky=W)
        self.start_button.grid(column=0, columnspan=2, row=3, sticky=E+W)

        self.choose_window.protocol("WM_DELETE_WINDOW", self.master.destroy)    # destroy master when chose option is closed

    def start_countdown(self):
        self.check_choice_input()


    def check_choice_input(self):
        if self.hours.get().isdigit() and self.minutes.get().isdigit() and self.action_choice.get():
            print("start")
        else:
            messagebox.showinfo("Make better choice", "Put valid number of hours, minutes and choose action.")

    def update_clock(self):
        now = datetime.now()
        time_to_end = self.time_end - now
        H_to_end = time_to_end.seconds//3600
        M_to_end = (time_to_end.seconds%(60*60))//60
        S_to_end = time_to_end.seconds%60
        if time_to_end.seconds//60 <= 4: self.canvas.itemconfigure(self.text, fill= 'red')
        angle_to_end = time_to_end.seconds / self.time_to_end_start.seconds
        angle_to_end = int(angle_to_end*360)
        self.canvas.itemconfigure(self.arc, extent=angle_to_end)
        time_to_end = (H_to_end, M_to_end, S_to_end)
        self.canvas.itemconfigure(self.text, text = "{:02d}:{:02d}:{:02d}".format(*time_to_end))
        # self.timer_to_end.configure(text="time to end: {}:{}:{}".format(*time_to_end))
        self.master.after(1000, self.update_clock)



def main():
    root = Tk()
    timer_app = Timer(root)
    root.mainloop()


if __name__ == "__main__": main()
