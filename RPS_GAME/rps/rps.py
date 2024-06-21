from tkinter import *
from PIL import Image, ImageTk
import random

# main window
root = Tk()
root.title('RPS Game')
root.configure(background='Pink')

# image
## Initialize client Images
crock = ImageTk.PhotoImage(Image.open('crock.png'))
cpaper = ImageTk.PhotoImage(Image.open('cpaper.png'))
cscissor = ImageTk.PhotoImage(Image.open('cscissor.png'))

## Initialize computer Images
rock_img = ImageTk.PhotoImage(Image.open('rock.png'))
paper_img = ImageTk.PhotoImage(Image.open('paper.png'))
scissor_img = ImageTk.PhotoImage(Image.open('scissor.png'))

# Indicate user and computer Side 
Client = Label(root, font=50, text='User', bg='White', fg='Black')
Computer = Label(root, font=50, text='Computer', bg='White', fg='Black')
Client.grid(row=0, column=4)
Computer.grid(row=0, column=0)

# User and Computer Images on display
computer_label = Label(root, image=paper_img, bg='White')
client_label = Label(root, image=cpaper, bg='White')

computer_label.grid(row=1, column=0)
client_label.grid(row=1, column=4)

# scores
client_scores = Label(root, text=0, font=100, bg='Black', fg='Yellow')
computer_scores = Label(root, text=0, font=100, bg='Black', fg='Yellow')

client_scores.grid(row=1, column=3)
computer_scores.grid(row=1, column=1)

# button for player
rock = Button(root, width=20, height=2, text='Rock', bg='Black', fg='Yellow', command=lambda: update_choice('rock'))
rock.grid(row=2, column=1)
paper = Button(root, width=20, height=2, text='Paper', bg='Black', fg='Yellow', command=lambda: update_choice('paper'))
paper.grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text='Scissor', bg='Black', fg='Yellow', command=lambda: update_choice('scissor'))
scissor.grid(row=2, column=3)

# Message for winning and losing
msg = Label(root, font=50, bg='Black', fg='Red')
msg.grid(row=1, column=2)

# Exit button
exit_button = Button(root, text='Exit', width=10, height=2, bg='Red', fg='White', command=root.quit)
exit_button.grid(row=4, column=2)

#update_msg 
def Update_msg(x):
    msg['text'] = x

# update scores
def Update_uscores():
    u_score = int(client_scores['text'])
    u_score += 1
    client_scores['text'] = str(u_score)

def Update_cscores():
    c_score = int(computer_scores['text'])
    c_score += 1
    computer_scores['text'] = str(c_score)

# update choices of client
computer_choices = ['rock', 'paper', 'scissors']

def update_choice(x):
    comp_choice = computer_choices[random.randint(0, 2)]
    if comp_choice == 'rock':
        computer_label.configure(image=rock_img)
    elif comp_choice == 'paper':
        computer_label.configure(image=paper_img)
    else:
        computer_label.configure(image=scissor_img)

    if x == 'rock':
        client_label.configure(image=crock)
    elif x == 'paper':
        client_label.configure(image=cpaper)
    else:
        client_label.configure(image=cscissor)

    checkwinner(x, comp_choice)

# check Winner
def checkwinner(client, computer):
    if client == computer:
        Update_msg('It\'s a Draw')
    elif client == 'rock':
        if computer == 'paper':
            Update_msg('You Lose')
            Update_cscores()
        else:
            Update_msg('You Win')
            Update_uscores()
    elif client == 'paper':
        if computer == 'scissors':
            Update_msg('You Lose')
            Update_cscores()
        else:
            Update_msg('You Win')
            Update_uscores()
    elif client == 'scissors':
        if computer == 'rock':
            Update_msg('You Lose')
            Update_cscores()
        else:
            Update_msg('You Win')
            Update_uscores()
    else:
        pass

root.mainloop()

