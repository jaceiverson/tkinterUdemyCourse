#Simon Game
#Icon GNU Lesser General Public License
import tkinter
from tkinter import RAISED, StringVar, ACTIVE, NORMAL, DISABLED
import random

#Define window
root = tkinter.Tk()
root.title('Simon')
root.iconbitmap('simon.ico')
root.geometry('400x400')

#Define fonts and colors
game_font1 = ('Arial', 12)
game_font2 = ('Arial', 8)
white = "#c6cbcd"
white_light = "#fbfcfc"
magenta = "#90189e"
magenta_light = "#f802f9"
cyan = "#078384"
cyan_light = "#00fafa"
yellow = "#9ba00f"
yellow_light = "#f7f801"
root_color = "#2eb4c6"
game_color = "#f6f7f8"
root.config(bg=root_color)

#Set global variables for game
time = 500
score = 0
game_sequence = []
player_sequence = []

#Define functions
def pick_sequence():
    """Pick the next value in the sequence.  Do not allow for repeated valued."""
    while True:
        value = random.randint(1,4)
        #Sequence is size 0, so take the value regardless
        if len(game_sequence) == 0:
            game_sequence.append(value)
            break
        #Make sure the current value is not the same as the last value in the sequence
        elif value != game_sequence[-1]:
            game_sequence.append(value)
            break
    
    #Now that the value is added to the sequence, play the sequence
    play_sequence()


def play_sequence():
    """Play the entire sequence for a given round by animating the buttons"""
    change_label('Playing!')

    #Without delay, all buttons will animate 'at' the same time.  The delay adds the 'time' interval to each
    #.after() such that the next button animates only after the previous one is complete.
    delay = 0
    for value in game_sequence:       
        if value == 1:
            root.after(delay, lambda:animate(white_button))
        elif value == 2:
            root.after(delay, lambda:animate(magenta_button))
        elif value == 3:
            root.after(delay, lambda:animate(cyan_button))
        elif value == 4:
            root.after(delay, lambda:animate(yellow_button))

        #Increment delay for next iteration of loop
        delay += time


def change_label(message):
    '''Update start button text and color to let the player know their status.'''
    start_button.config(text=message)

    if message == 'Wrong!':
        start_button['bg'] = 'red'
    else:
        start_button['bg'] = game_color


def animate(button):
    """Animate a given button by changing its color"""
    button.config(state=ACTIVE)
    root.after(time, lambda:button.config(state=NORMAL))


def set_difficulty():
    """Use radio buttons to set difficulty.  Difficulty affects time between button flash"""
    global time

    #Change the time (difficulty) based off the value of the radio buttons
    if difficulty.get() == 'Easy':
        time = 1000
    elif difficulty.get() == "Medium":
        time = 500
    else:
        time = 200


def press(value):
    """Simulate pressing a button for player.  1=white, 2=magenta, 3=cyan, 4=yellow"""
    #Add the players press to the player_sequence
    player_sequence.append(value)

    #If the current "round" is over, check to see if the player entered the correct sequence of button presses
    if len(player_sequence) == len(game_sequence):
        check_round()


def check_round():
    """Determine if the player entered the correct sequence of button presses for a round."""
    global player_sequence
    global game_sequence
    global score

    #The players is correct so change label, update score, wait, then start next round
    if player_sequence == game_sequence:
        change_label('Correct!')
        score += len(player_sequence) + int(1000/time)
        root.after(500, pick_sequence)
    #The player is incorrect so change label, update score, disable buttons, and reset for new game
    else:
        change_label('Wrong!')
        score = 0
        disable()
        #The game is over, so create a blank game_sequence to play again.
        game_sequence = []
        #wait 2 seconds then change message
        root.after(2000, lambda: change_label("New Game"))
        
    #Regardless if the player is correct, the player_sequence needs to be blank for the next round/new game.
    player_sequence = []

    #Update the score label.
    score_label.config(text="Score: " + str(score))


def disable():
    '''Disable all buttons so they can't accidentaly be pressed'''
    white_button.config(state=DISABLED)
    magenta_button.config(state=DISABLED)
    cyan_button.config(state=DISABLED)
    yellow_button.config(state=DISABLED)


def enable():
    '''Enable all buttons to state the game and pick the first value in the sequence'''
    white_button.config(state=NORMAL)
    magenta_button.config(state=NORMAL)
    cyan_button.config(state=NORMAL)
    yellow_button.config(state=NORMAL)

    #Pick a value!
    pick_sequence()


'''
def test():
    pick_sequence()
    print(game_sequence)
'''

#GUI Layout
#Make frames
info_frame = tkinter.Frame(root, bg=root_color)
game_frame = tkinter.LabelFrame(root, bg=game_color)
info_frame.pack(pady=(10,20))
game_frame.pack()

#Layout for the info frame
start_button = tkinter.Button(info_frame, text="New Game", font=game_font1, bg=game_color, command=enable)
score_label = tkinter.Label(info_frame, text="Score: " + str(score), font=game_font1, bg=root_color)
start_button.grid(row=0, column=0, padx=20, ipadx=30)
score_label.grid(row=0, column=1)

#Layout for the game frame
#Make the game buttons
white_button = tkinter.Button(game_frame, text="", bg=white, activebackground=white_light, borderwidth=3, relief=RAISED, command=lambda:press(1), state=DISABLED)
magenta_button = tkinter.Button(game_frame, text="", bg=magenta, activebackground=magenta_light, borderwidth=3, relief=RAISED, command=lambda:press(2), state=DISABLED)
cyan_button = tkinter.Button(game_frame, text="", bg=cyan, activebackground=cyan_light, borderwidth=3, relief=RAISED, command=lambda:press(3), state=DISABLED)
yellow_button = tkinter.Button(game_frame, text="", bg=yellow, activebackground=yellow_light, borderwidth=3, relief=RAISED, command=lambda:press(4), state=DISABLED)

white_button.grid(row=0, column=0, columnspan=2, padx=10, pady=10, ipadx=60, ipady=50)
magenta_button.grid(row=0, column=2, columnspan=2, padx=10, pady=10, ipadx=60, ipady=50)
cyan_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, ipadx=60, ipady=50)
yellow_button.grid(row=1, column=2, columnspan=2, padx=10, pady=10, ipadx=60, ipady=50)

#Make difficutly buttons  
difficulty = StringVar()
difficulty.set('Medium')
tkinter.Label(game_frame, text="Difficulty:", font=game_font2, bg=game_color).grid(row=2, column=0)
tkinter.Radiobutton(game_frame, text="Easy", variable=difficulty, value="Easy", font=game_font2, bg=game_color, command=set_difficulty).grid(row=2, column=1)
tkinter.Radiobutton(game_frame, text="Medium", variable=difficulty, value="Medium", font=game_font2, bg=game_color, command=set_difficulty).grid(row=2, column=2)
tkinter.Radiobutton(game_frame, text="Hard", variable=difficulty, value="Hard", font=game_font2, bg=game_color, command=set_difficulty).grid(row=2, column=3)

#Call the root window's main loop
root.mainloop()