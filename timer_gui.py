from tkinter import *
from datetime import datetime
from datetime import timedelta



class Timer():
    def __init__(self, master):
        self.master = master
        self.master.title("Timer")
        self.master.resizable(False, False)
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(hours=0.1)
        self.time_to_end_init = self.end_time - self.start_time
        self.label = Label(master, text="")
        self.timer_label = Label(master, text="start:  " + self.start_time.strftime("%H:%M:%S"))
        self.timer_end = Label(master, text="end time:  " + self.end_time.strftime("%H:%M:%S"))

        self.canvas = Canvas(master)
        self.canvas.pack()
        self.canvas.config(width=300, height=300, background="black")

        self.arc = self.canvas.create_arc(10, 10, 290, 290)
        self.canvas.itemconfigure(self.arc, start = 90, extent = 270, fill = 'red4', width = 0)
        self.oval = self.canvas.create_oval(30, 30, 270, 270, fill='black')
        self.text = self.canvas.create_text(150, 150, text = '', font = ('Courier', 32, 'bold'), fill="white")
        self.update_clock()





    def update_clock(self):
        now = datetime.now()
        time_to_end = self.end_time - now
        H_to_end = time_to_end.seconds//3600
        M_to_end = (time_to_end.seconds%(60*60))//60
        S_to_end = time_to_end.seconds%60
        if time_to_end.seconds//60 <= 4: self.canvas.itemconfigure(self.text, fill= 'red')
        angle_to_end = time_to_end.seconds / self.time_to_end_init.seconds
        angle_to_end = int(angle_to_end*360)
        self.canvas.itemconfigure(self.arc, extent=angle_to_end)
        time_to_end = (H_to_end, M_to_end, S_to_end)
        self.label.configure(text="time now: " + now.strftime("%H:%M:%S"))
        self.canvas.itemconfigure(self.text, text = "{:02d}:{:02d}:{:02d}".format(*time_to_end))
        # self.timer_to_end.configure(text="time to end: {}:{}:{}".format(*time_to_end))
        self.master.after(1000, self.update_clock)



def main():
    root = Tk()
    timer_app = Timer(root)
    root.mainloop()


if __name__ == "__main__": main()
