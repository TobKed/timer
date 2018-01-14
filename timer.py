import ctypes
import os
import time
import asciinumbers as asci
if os.name == 'nt':
    import winsound
    
def choice_menu():
    global choice
    try:
        choice = int(input("choice: \n 1 - LOCK \n 2 - SHUTDOWN \n"))
        if choice not in [1, 2]:
            raise NameError("no such option")   
    except:
        print("try again")
        time.sleep(0.5)
        os.system('cls')
        choice_menu()
        
def choice_time():
    global timer
    try:
        timer = int(input("TIME in hours: \n"))*3600
        timer += int(input("TIME in minutes: \n"))*60
        if timer <= 0:
            raise NameError("negative time") 
    except:
        print("wrong time input")
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        choice_time()
      
def print_timer():
    choice_str = {1:"lock", 2:"shutdown"}
    os.system('cls' if os.name == 'nt' else 'clear')
    
    hours = ""
    hours_show = False
    if timer//3600 >= 1: 
        hours_show = True
    
    for x in range(timer, -1, -1):
        if hours_show:
            hours = str(x//3600).zfill(2) + ":"
        minutes = str((x%3600)//60).zfill(2) + ":"
        seconds = str(x%60).zfill(2)
        time_to_action = ' ' + hours + minutes + seconds
        asci.print_ASCII(time_to_action)
        info = " to " + choice_str[choice] + " "
        print(info.center(76, "."))
        if choice == 1 and x <= 5:
            if os.name == 'nt':
                winsound.Beep(2500, 500)
                time.sleep(0.5)
            else:
                time.sleep(1)
        else:
            time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')


def main():
    choice_menu()
    choice_time()
    print_timer()

    if choice == 1:
        if os.name == 'nt':
            winsound.Beep(2500, 1500)
            ctypes.windll.user32.LockWorkStation()
        else:
            os.system('cinnamon-screensaver-command -l')
    if choice == 2:
        os.system('shutdown -s' if os.name == 'nt' else 'shutdown +1 "Your system will shutdwon in a minute"')


if __name__ == "__main__": main()

 
 
