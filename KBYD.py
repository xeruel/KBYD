# KBYD 1.0.1 - Simple Bulls and Cows Game
import os
import random
import time

# digit variables
global digits

# else variables
global gamemode
global difficulty
global timessetting
global gameend
global gamewin
global ihistory
global rhistory
global usr

usr = []
gameend = 0
ihistory = []
rhistory = []

# clear console
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# main title
def maintitle():
    global gamemode

    clear()
    print("KBYD 1.0.1 - Simple Bulls and Cows Game")
    print("Please Select Game Mode\n")
    print("1. Baseball Rule - You can try 9 times.")
    print("2. Unlimited Rule - You can try until to guess right.")
    print("3. Custom Rule - You can set guessing times on your own.")
    print("H. How to Play")
    print("L. License")
    print("E. Exit\n")
    print("If you don't select anything, The game will start with Baseball Rule.\n")

    print("KBYD  Copyright (C) 2021.  Xeruel a.k.a. MochaSyrup")
    print("This is free software, and you are welcome to redistribute it under certain conditions; type 'L' for details.\n")

    gamemode = input("Please input option here: ")
    if gamemode == "E" or gamemode == "e":
        exit()
    elif gamemode == "H" or gamemode == "h":
        helptext()
    elif gamemode == "L" or gamemode == "l":
        license()
    else:
        if gamemode != "1" and gamemode !="2" and gamemode != "3":
            gamemode = "1"
        else: pass
        difficultyset()

# how to play
def helptext():
    clear()
    print("KBYD 1.0.1 - Simple Bulls and Cows Game")
    print("How to Play\n")
    print("KBYD is a simple Bulls and Cows Game.\n")
    print("When the game starts, the computer randomly generates 3 to 5 digit-number.")
    print("You have to guess that number until you run out of chances.\n")
    print("If you press Enter after entering a number, the number and result are recorded in the history field as follows.\n")
    print("[c, d, e, f, g] / hAiB\n")
    print("A means both number and position match.")
    print("B means the numbers match but the positions do not.")
    print("So, 1A2B means that there is one digit that matches both the number and position, and two digit that matches the number but does not match the position.")
    print("The game will repeat until you run out of chances or you have guessed all the numbers.\n")
    print("Good Luck.")

    tempinput = input("\nPress Enter to return into start page.")
    if tempinput == "": resetphase()
    else: resetphase()

# license
def license():
    clear()
    print("KBYD 1.0.1 - Simple Bulls and Cows Game")
    print("License\n")
    print("KBYD is a simple Bulls and Cows Game.")
    print("Copyright (C) 2021.  Xeruel a.k.a. MochaSyrup\n")
    print("This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.")
    print("This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.\n")
    print("You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.\n")

    tempinput = input("\nPress Enter to return into start page.")
    if tempinput == "": resetphase()
    else: resetphase()

# difficulty
def difficultyset():
    global difficulty

    clear()
    print("KBYD 1.0.1 - Simple Bulls and Cows Game")
    print("Please Select difficulty\n")
    print("1. Easy - 3-digit number")
    print("2. Normal - 4-digit number")
    print("3. Hard - 5-digit number\n")
    print("If you don't select anything, It will start with Easy setting.")
    
    difficulty = input("Please input option here: ")
    if difficulty != "1" and difficulty !="2" and difficulty != "3":
        difficulty = "1"
    else: pass
    
    randomphase()

# roll the number
def randomphase():
    global difficulty
    global digits

    digits = random.sample(range(0,10), 2+int(difficulty))
    random.shuffle(digits)
    timesset()

# set trying times
def timesset():
    global gamemode
    global timessetting

    if gamemode == "1":
        timessetting = 9
        gamestart()
    elif gamemode == "3":
        clear()
        print("KBYD 1.0.1 - Simple Bulls and Cows Game")
        print("Please Set your own guessing times.\n")
        print("If you don't select anything, It will start with Baseball Rule(9 times).")

        tempinput = input("Please input digits here: ")
        if tempinput == '':
            timessetting = 9
        else:
            timessetting = int(tempinput)
        gamestart()
    else:
        timessetting = -1
        gamestart()


# game start
def gamestart():
    global timessetting
    global gameend

    while True:
        if gameend == 1:
            gameresult()
            break
        else:
            gameanswer()
        
    resetphase()

# input answer
def gameanswer():
    global digits
    global timessetting
    global ihistory
    global rhistory
    global usr

    usr = []
    fakevalue = 0

    clear()
    print("KBYD 1.0.1 - Simple Bulls and Cows Game")
    print("Please input your answer.\n")

    if timessetting == 1:
        print("You have 1 chance left.")
    elif timessetting == -1: pass
    else:
        print("You have", timessetting, "chances left.")

    print("History\n")
    if len(rhistory) == 0:
        pass
    else:
        for i in range(0, len(rhistory)):
            print(str(ihistory[i]), '/', str(rhistory[i]))

    tempinput = input("\nPlease input digits here: ")
    if tempinput == "":
        gameanswer()
    else:
        usr = list(map(int, list(tempinput)))
        if len(usr) == len(digits):
            for i in range(0,10):
                if usr.count(i) == 1 or usr.count(i) == 0: pass
                else:
                    fakevalue = 1
            if fakevalue == 0: gameprocess()
            else: gameanswer()
        else: gameanswer()

# game process
def gameprocess():
    global difficulty
    global timessetting
    global gameend
    global gamewin
    global digits
    global usr
    global ihistory
    global rhistory

    a = 0
    b = 0

    for i in usr:
        if digits.count(i) == 1:
            if usr.index(i) == digits.index(i):
                a += 1
            else:
                b += 1
        elif digits.count(i) == 0: pass
        else:
            print("An error has occurred. Program will return into start page in 5 seconds...")
            time.sleep(5)
            resetphase()
    
    if len(ihistory) == 20:
        ihistory.pop(0)
    else: pass

    if len(rhistory) == 20:
        rhistory.pop(0)
    else: pass

    ihistory.append(str(usr))
    rhistory.append(str(a)+'A'+str(b)+'B')

    if str(rhistory[-1]) == str(int(difficulty)+2)+"A0B":
        gameend = 1
        gamewin = 1
    else: pass

    if timessetting == -1: pass
    else:
        timessetting -= 1
        if timessetting == 0:
            gameend = 1
        else: pass

# game result
def gameresult():
    if gamewin == 0:
        print("\nThat's too bad. You've lost.")
    elif gamewin == 1:
        print("\nCongratulation! You won!")
    
    print("Correct answer was", digits)

    tempinput = input("\nPress Enter to restart the game.")
    if tempinput == "": resetphase()
    else: resetphase()

# game reset
def resetphase():
    global gamemode
    global difficulty
    global timessetting
    global gameend
    global gamewin
    global digits
    global usr
    global ihistory
    global rhistory

    gamemode = 0
    difficulty = 0
    timessetting = 0
    gameend = 0
    gamewin = 0
    digits = []
    usr = []
    ihistory = []
    rhistory = []

    maintitle()

resetphase()
maintitle()
