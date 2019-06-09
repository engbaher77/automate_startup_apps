import pyautogui
import sys
import psutil    
import time

#Point(x=204, y=62)  ::: Chrome task bar upper left
#Point(x=323, y=750) ::: Chrome Icon
#Point(x=360, y=750) ::: Folder Icon
#Point(x=418, y=742) ::: Git Icone
#Point(x=466, y=745) ::: Visual studio
#Point(x=290, y=72)  ::: Folder address bar


def check():
    result = input("Hello! Mr.Baher What're you Gonna Do now?")

    if result == "programming":
        programing()
    elif result == "cursor position":
        cursor_postion()
    elif result == "site work":
        site_work()
    elif result == "new layout":
        new_layout()
    else:
        return False
    return result

def cursor_postion():
    print(pyautogui.position())
    #print(time_delay())


def time_delay(program):
    is_runing = False
    counter = 0
    while is_runing == False:
        is_runing = program in (p.name() for p in psutil.process_iter())
        if is_runing == True:
            break   
        
        time.sleep(1)
        counter += 1
    #print (counter)
    return counter


def test_program(program_name, how_open):
    if how_open == "Start Button" or "start button":    
        print("We are testing now !!", program_name)
        pyautogui.typewrite(["win"]) 
        time.sleep(2)
        pyautogui.typewrite(program_name)
        time.sleep(5)
        pyautogui.typewrite(["enter"])   
        time.sleep(3)
        is_runing = input("Is %s started scuccessfully??\n" % (program_name))
        print(is_runing)
    else:
        pass
 

def new_layout():
    how_open = input("How can we open the program::: Start Button or Run command or help for more info?? \n")

    if how_open == "Start Button" or "start button":
        print("start button activated")
        program_name = input("Enter program name as you type in start menu!! help for more info??\n")
        print("Your program name is :::", program_name)
        test_program(program_name,how_open)
    elif how_open == "Run Command" or "run command":
        print("run command is activated")
        program_name = input("Enter command or program name as you type in run window!! help for more info??\n")
        print("Your command/program is :::", program_name)

    else:
        print("you entered incorrect choise !!")
    


def programing():

   #explorer 
    pyautogui.hotkey("win", "r")
    time.sleep(2)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.typewrite(r"D:\Sources\Python\Projects")
    pyautogui.typewrite(["enter"])
    time.sleep(time_delay("explorer.exe"))
    time.sleep(2)
    #pyautogui.hotkey("win", "right")

    #chrome 
    pyautogui.hotkey("win", "r")
    time.sleep(2)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.typewrite(r"chrome.exe")
    pyautogui.typewrite(["enter"])
    time.sleep(time_delay("chrome.exe"))
    time.sleep(2)
    #pyautogui.hotkey("win", "left")

    #Vs code
    pyautogui.typewrite(["win"]) 
    time.sleep(2)
    pyautogui.typewrite("visual studio")
    time.sleep(5)
    pyautogui.typewrite(["enter"])   
    time.sleep(3) 
    

    #pyautogui.hotkey("ctrl", "a")
    #pyautogui.typewrite(["backspace"])
    #pyautogui.typewrite("google.com")
    #pyautogui.typewrite(["enter"])



def site_work():

    
   #explorer 
    pyautogui.hotkey("win", "r")
    time.sleep(2)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.typewrite(r"explorer.exe D:\Aiactive\B-A-H-E-R")
    pyautogui.typewrite(["enter"])
    time.sleep(time_delay("explorer.exe"))
    time.sleep(2)
    #pyautogui.hotkey("win", "right")

    #chrome 
    pyautogui.hotkey("win", "r")
    time.sleep(2)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.typewrite(r"chrome.exe")
    pyautogui.typewrite(["enter"])
    time.sleep(time_delay("chrome.exe"))
    time.sleep(2)
    #pyautogui.hotkey("win", "left")

    #Command prompt
    pyautogui.hotkey("win", "r")
    time.sleep(2)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.typewrite("cmd")
    pyautogui.typewrite(["enter"])



if __name__ == "__main__":
    errormsg = "Error Answer me again!!"
    succmsg = "Done !!"

    result = check()
    print(result)

    while result == 0:
        print(errormsg)
        check()
    else:
        print(succmsg)