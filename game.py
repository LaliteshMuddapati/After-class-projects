from tkinter import *
import random

window=Tk()
window.title('Rock, Paper Scissors... Shoot!')
window.configure(bg='orange')
window.geometry('600x400')

l1=Label(window, text="Waiting for your turn", bg='white', font=("Arial", 16, "bold"))
l1.pack()


def game(user):
    outcomes=["rock", "paper", "scissors"]
    computer=random.choice(outcomes)
    if user=="scissors" and computer=="paper":
        l1.config(text=f"You win, computer played {computer}")
    elif user=="rock" and computer=="scissors":
        l1.config(text=f"You win, computer played {computer}")
    elif user=="paper" and computer=="rock":
        l1.config(text=f"You win, computer played {computer}")
    elif user=="scissors" and computer=="rock":
        l1.config(text=f"You lose, computer played {computer}")
    elif user=="rock" and computer=="paper":
        l1.config(text=f"You lose, computer played {computer}")
    elif user=="paper" and computer=="scissors":
        l1.config(text=f"You lose, computer played {computer}")
    else:
        l1.config(text=f"Tie, computer played {computer}")

def r():
    game("rock")
    
def p():
    game("paper")

def s():
    game("scissors")

b1=Button(window, text="Rock", bg='white',font=("Arial", 20, "bold"), command=r)
b1.pack(pady=10)
b1=Button(window, text="Paper", bg='white',font=("Arial", 20, "bold"), command=p)
b1.pack(pady=10)
b1=Button(window, text="Scissors", bg='white',font=("Arial", 20, "bold"), command=s)
b1.pack(pady=10)

window.mainloop()