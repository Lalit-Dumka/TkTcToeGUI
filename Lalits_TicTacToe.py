'''
The Tic-Tac-Toe
This program uses 2 Libraries :
    1. Tkinter - For making the Graphical User Interface.
    2. itertools - For general mathematical list Operations
This game is for two players.
Date : 15/April/2020
Author : Lalit Dumka
Version : v0.1.0
 '''

# Importing Modules 
from tkinter import *
from itertools import combinations

# Setting general Toplevel Window 
app = Tk()
app.title("Lalit's Tic-Tac-Toe")  # The name of Window
app.geometry("500x500+235+100")     # Initial size of Window

# Initializing Game Variables
winner = None
available = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] # No of boxes available to the players
xLst = [] # No of boxes with X filled.
oLst=[]   # No of boxes with O.
chance = 'u'  # variable to decide weather the box will be filled with X or O

# Defining functions for the Game
def replace(buttonText, ox):
    """
    This function replaces the Button with a label of desired text('X' or 'O')

    Arguments:
        buttonText {string} -- Text of the button to replace. [Event.widget.cget('text')]
        ox {string} -- String with which to replace the Button ---- 'X' or 'O'
    """    
    if buttonText == '1':
        Label(tableFrame, text=ox, bg='cyan', bd=5, font=(
            "Comic Sans MS", 38)).place(x=20, y=20, width=90, height=90)
    elif buttonText == '2':
        Label(tableFrame, text=ox, bg='cyan', bd=5, font=(
            "Comic Sans MS", 38)).place(x=110, y=20, width=90, height=90)
    elif buttonText == '3':
        Label(tableFrame, text=ox, bg='cyan', bd=5, font=(
            "Comic Sans MS", 38)).place(x=200, y=20, width=90, height=90)
    elif buttonText == '4':
        Label(tableFrame, text=ox, bg='cyan', bd=5, font=(
            "Comic Sans MS", 38)).place(x=20, y=110, width=90, height=90)
    elif buttonText == '5':
        Label(tableFrame, text=ox, bg='cyan', bd=5, font=(
            "Comic Sans MS", 38)).place(x=110, y=110, width=90, height=90)
    elif buttonText == '6':
        Label(tableFrame, text=ox, bg='cyan', bd=5, font=(
            "Comic Sans MS", 38)).place(x=200, y=110, width=90, height=90)
    elif buttonText == '7':
        Label(tableFrame, text=ox, bg='cyan', bd=5, font=(
            "Comic Sans MS", 38)).place(x=20, y=200, width=90, height=90)
    elif buttonText == '8':
        Label(tableFrame, text=ox, bg='cyan', bd=5, font=(
            "Comic Sans MS", 38)).place(x=110, y=200, width=90, height=90)
    elif buttonText == '9':
        Label(tableFrame, text=ox, bg='cyan', bd=5, font=(
            "Comic Sans MS", 38)).place(x=200, y=200, width=90, height=90)
    else:
        pass

def uChance(Event):
    """
    This function is called when any of the Button is Pressed.
    It check the chance variable and replaces the buttons as Desired(By the programmer)
    """    
    global chance
    buttonTxt = Event.widget.cget('text')
    Event.widget.place_forget()
    if chance == 'u':
        replace(buttonTxt, 'X')
        xLst.append(buttonTxt)
        chance='c'
    elif chance == 'c':
        replace(buttonTxt, 'O')
        oLst.append(buttonTxt)
        chance = 'u'
    xLst.sort()
    oLst.sort()
    available.remove(buttonTxt)
    checkWin(xLst,oLst)

def checkWin(xList,oList):
    '''
    This function checks wheather the winning conditions are met and by which side - and then generates a label with the WINNER NAME and Message.
    It also check if the game is tied.
    '''
    global available
    global chance
    winConditions = [('1','2','3'),('4','5','6'),('7','8','9'),('1','4','7'),('2','5','8'),('3','6','9'),('1','5','9'),('3','5','7')]
    combX = []
    combO = []
    if chance == 'c':
        for i in range(1,len(xList)+1):
            a=combinations(xList,i)
            for j in list(a):
                combX.append(j)
    elif chance == 'u':
        for i in range(1,len(oList)+1):
            a=combinations(oList,i)
            for j in list(a):
                combO.append(j)
    
    if available == []:
        tableFrame.place_forget()
        winFrame.place(x=50, y=140, width=402, height=300)
        winLabel.config(text = f'Game Over !!!!\n Game Tied..... ')
        winLabel.place(x=5,y=5)
    else:
        for i in winConditions:
            for j in combX:
                if i == j :
                    tableFrame.place_forget()
                    winFrame.place(x=50, y=140, width=402, height=300)
                    winLabel.config(text = f'Game Over !!!!\n  Player with X \n   Won the GAME ... ')
                    winLabel.place(x=5,y=5)
                    break
            for k in combO:
                if i == j :
                    tableFrame.place_forget()
                    winLabel.place(x=5,y=5)
                    winLabel.config(text = f'Game Over !!!!\n  Player with O \n   Won the GAME ... ')
                    winFrame.place(x=50, y=140, width=402, height=300)
                    break
####################################################################################################### Creating the Tkinter Widgets Required for the GUI
Label(app,text = "Lalit's Tic-Tac-Toe",border=5,fg='blue',font = ("Comic Sans MS", 38)).place(x=10,y=20)

tableFrame = Frame(app, border=5, relief=GROOVE)
tableFrame.place(x=75, y=160, width=340, height=320)

winFrame = Frame(app, border=5, relief=GROOVE)

winLabel = Label(winFrame,text = "",font=("Comic Sans MS", 30))

one = Button(tableFrame, text='1', bg='cyan', fg='cyan', bd=5)
one.place(x=20, y=20, width=90, height=90)
one.bind("<Button-1>", uChance)

two=Button(tableFrame, text="2", bg='cyan', fg='cyan', bd=5)
two.place(x=110, y=20, width=90, height=90)
two.bind("<Button-1>", uChance)

three=Button(tableFrame, text='3', bg='cyan', fg='cyan', bd=5)
three.place(x=200, y=20, width=90, height=90)
three.bind("<Button-1>", uChance)

four=Button(tableFrame, text='4', bg='cyan', fg='cyan', bd=5)
four.place(x=20, y=110, width=90, height=90)
four.bind("<Button-1>", uChance)

five=Button(tableFrame, text='5', bg='cyan', fg='cyan', bd=5)
five.place(x=110, y=110, width=90, height=90)
five.bind("<Button-1>", uChance)

six=Button(tableFrame, text='6', bg='cyan', fg='cyan', bd=5)
six.place(x=200, y=110, width=90, height=90)
six.bind("<Button-1>", uChance)

seven=Button(tableFrame, text='7', bg='cyan', fg='cyan', bd=5)
seven.place(x=20, y=200, width=90, height=90)
seven.bind("<Button-1>", uChance)

eight=Button(tableFrame, text='8', bg='cyan', fg='cyan', bd=5)
eight.place(x=110, y=200, width=90, height=90)
eight.bind("<Button-1>", uChance)

nine=Button(tableFrame, text='9', bg='cyan', fg='cyan', bd=5)
nine.place(x=200, y=200, width=90, height=90)
nine.bind("<Button-1>", uChance)

# Calling the Tkinter Mainloop Function
app.mainloop()