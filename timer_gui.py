from tkinter import *
import time



class Timer():
    def __init__(self, master):
        self.master = master
        self.label = Label(master, text="")
        self.label.pack()
        self.master.after(1000, self.update_clock)

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.master.after(1000, self.update_clock)





def main():
    root = Tk()
    timer_app = Timer(root)
    root.mainloop()


if __name__ == "__main__": main()
