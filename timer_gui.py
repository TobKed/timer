from tkinter import *
import time
from datetime import datetime
from datetime import timedelta



class Timer():
    def __init__(self, master):
        self.master = master
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(hours=3)
        self.label = Label(master, text="")
        self.timer_label = Label(master, text="start:  " + self.start_time.strftime("%H:%M:%S"))
        self.timer_end = Label(master, text="end time:  " + self.end_time.strftime("%H:%M:%S"))
        self.timer_to_end = Label(master, text="")
        self.label.pack(anchor=E)
        self.timer_label.pack(anchor=E)
        self.timer_end.pack(anchor=E)
        self.timer_to_end.pack(anchor=E)
        self.master.after(1000, self.update_clock)

    def update_clock(self):
        now = datetime.now()
        time_to_end = self.end_time - now
        H_to_end = time_to_end.seconds//3600
        M_to_end = (time_to_end.seconds%(60*60))//60
        S_to_end = time_to_end.seconds%60
        time_to_end = (H_to_end, M_to_end, S_to_end)
        self.label.configure(text="time now: " + now.strftime("%H:%M:%S"))
        self.timer_to_end.configure(text="time to end: {}:{}:{}".format(*time_to_end))
        self.master.after(1000, self.update_clock)



def main():
    root = Tk()
    timer_app = Timer(root)
    root.mainloop()


if __name__ == "__main__": main()
