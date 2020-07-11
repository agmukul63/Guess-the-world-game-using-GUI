#Devloped By Team Zeetron Network"

import tkinter
from tkinter import*
import random     # library that we use in order to choose on random words from a list of words
import time

global words, word, turns, guesses, s, canvas
guesses = ''
turns= 8   # any number of turns can be used here
s=" "
def reset():
    global words, word, turns, guesses, s, canvas, root
    root.destroy()
    guesses = ''
    turns = 8  # any number of turns can be used here
    s = " "
    main()


def can1():
    global canvas
    canvas.create_rectangle(50, 20, 170, 110, outline="blue", fill="white",width=3)
    canvas.grid(row=15, column=1)

def can2():
    global canvas
    canvas.create_rectangle(170, 40, 250, 110, outline="blue", fill="white", width=3)
    canvas.grid(row=15, column=1)

def can3():
    global canvas
    canvas.create_oval(60, 95, 90, 125, outline="blue",fill="blue", width=2)
    canvas.grid(row=15, column=1)

def can4():
    global canvas
    canvas.create_oval(160, 95, 190, 125, outline="blue", fill="blue", width=2)
    canvas.grid(row=15, column=1)

def can5():
    global canvas
    canvas.create_rectangle(180, 50, 230, 65, outline="blue", fill="white", width=3)
    canvas.grid(row=15, column=1)

def can6():
    global canvas
    canvas.create_rectangle(100, 10, 120, 20, outline="blue", fill="red", width=3)
    canvas.grid(row=15, column=1)

def can7():
    global canvas
    canvas.create_rectangle(90, 35, 130, 55, outline="red", fill="red", width=2)
    canvas.grid(row=15, column=1)

def can8():
    global canvas
    canvas.create_rectangle(100, 25, 120, 65, outline="red", fill="red", width=2)
    canvas.grid(row=15, column=1)

def setword():
    global word, root
    word = Player1_field.get()  # take a 1st player name from Player1_field entry box
    word = word.lower()  # converted all letters into lower case
    word.replace(" ", "")  # replace any space with empty string
    print("\n\n\n--------------PLAYER 2 --------------\nGuess a letter and write in your entry box and press submit letter BUTTON")
    print("Good Luck ! PLAYER 2")

def logic():
    Label(root,bg='yellow').grid(row=3,column=0)  # For Heading
    Label(root, text='Guess the word:', font="Helvetica 17 italic", bg='yellow', fg='blue').grid(row=4,column=0)  # For Heading
    global guesses, turns,s
    failed = 0   # counts the number of times a user fails
    guess = Player2_field.get()  # if user has input the wrong alphabet then it will ask user to enter another alphabet
    guesses += guess   # every input character will be stored in guesses
    for i, char in enumerate(word):   # all characters from the input word taking one at a time.
        if char in guesses:     # comparing that character with the character in guesses
            Label(root, text=char,font="Helvetica 17 italic",fg="blue", bg='yellow').grid(row=i+5,column=0)
        else:
            Label(root, text="*",font="Helvetica 17 italic",fg="blue", bg='yellow').grid(row=i+5,column=0)
            failed += 1  # for every failure 1 will be incremented in failure
    if failed == 0:  # user will win the game if failure is 0 and 'You Win' will be given as output
        Label(root, text="YOU WIN!",font="Helvetica 25 bold", bg='yellow').grid(row=13,column=1)
        Label(root, text="The word is: "+ word, bg='yellow').grid(row=14,column=1)  # this print the correct word

    if guess not in word:  # check input with the character in word

        turns -= 1
        Label(root, text="Wrong Guesses : ",font="Helvetica 17 italic",fg="green", bg='yellow').grid(row=17, column=0) # if the character doesn’t match the word then “Wrong” will be given as output
        s= s + "  " + guess
        Label(root, text=s,font="Helvetica 17 italic",fg="green", bg='yellow').grid(row=18,column=0)
        Label(root, bg="yellow").grid(row=29, column=0)
        Label(root,bg="yellow").grid(row=30,column=0)
        Label(root, text="You have " + str(turns) +' attempts left',font="Helvetica 10 italic", bg='yellow').grid(row=31,column=1) # this will print the number of turns left for the user

        if turns==7:
            can1()
        if turns==6:
            can2()
        if turns==5:
            can3()
        if turns==4:
            can4()
        if turns==3:
            can5()
        if turns==2:
            can6()
        if turns==1:
            can7()
        if turns== 0:
            can8()
            Label(root, text="YOU LOSE!",font="Helvetica 25 bold", bg='yellow').grid(row=13,column=1)
            Label(root, text="The word is: " + word, bg='yellow').grid(row=14, column=1)  # this print the correct word
        if turns == -1:
            root.destroy()

def main():
    global root, Player1_field, Player2_field, canvas
    root = Tk()  # Create a GUI window
    root.configure(background='yellow')  # Set the background colour of GUI window
    root.geometry("700x800")  # Set the configuration of GUI window
    root.title("Barry's Guess The Word Game")  # set the name of tkinter GUI window
    canvas = Canvas(root, bg="yellow", bd=2, width=300, height=150)

    print("--------------PLAYER 1 --------------\n(Make sure PLAYER 2 is not peaking!\nEnter your word  in your entry box and press submit word BUTTON\n(if it has a space, use '-',e.g. ice-cream)")
    Label(root, text="PLAYER 1 Entry Box", font='15', fg='black', bg='yellow').grid(row=1, column=0, sticky="E")
    Player1_field = Entry(root)  # Create a text entry box for filling or typing the information.
    Player1_field.grid(row=1, column=1, ipadx="20")  # ipadx keyword argument set width of entry space .
    Button(root, text="Submit Word", bg="red", fg="black", command=setword).grid(row=1,
                                                                                 column=2)  # Create a Submit Button and attached to tell_status function

    Label(root, text="PLAYER 2 Entry Box", font='15', fg='black', bg='yellow').grid(row=2, column=0, sticky="E")
    Player2_field = Entry(root)  # Create a text entry box for filling or typing the information.
    Player2_field.grid(row=2, column=1, ipadx="20")  # ipadx keyword argument set width of entry space .
    Button(root, text="Submit letter", bg="red", fg="black", command=logic).grid(row=2,column=2)  # Create a Submit Button and attached to tell_status function

    Button(root, text="RESET", bg="white", fg="red", command=reset).grid(row=32, column=1)

    root.mainloop()  # Start the GUI


if __name__ == "__main__":   # Driver code
    main()


