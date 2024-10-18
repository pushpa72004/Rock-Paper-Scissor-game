import random
import tkinter as tk
from tkinter import messagebox

choices = ['rock', 'paper', 'scissors']


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"



def play_round(user_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)


    computer_choice_label.config(text=f"Computer chose: {computer_choice.capitalize()}")
    result_label.config(text=result)


    if result == "You win!":
        scores['user'] += 1
    elif result == "You lose!":
        scores['computer'] += 1
    score_label.config(text=f"Score: You {scores['user']} - {scores['computer']} Computer")



def reset_game():
    scores['user'] = 0
    scores['computer'] = 0
    result_label.config(text="")
    computer_choice_label.config(text="")
    score_label.config(text="Score: You 0 - 0 Computer")



window = tk.Tk()
window.title("Rock-Paper-Scissors")
window.geometry("400x300")
window.configure(bg='#f0f0f0')

tk.Label(window, text="Choose Rock, Paper, or Scissors:", bg='#f0f0f0', font=("Arial", 16)).pack(pady=10)


button_frame = tk.Frame(window, bg='#f0f0f0')
button_frame.pack(pady=10)


tk.Button(button_frame, text="Rock", command=lambda: play_round('rock'), width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Paper", command=lambda: play_round('paper'), width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Scissors", command=lambda: play_round('scissors'), width=10).pack(side=tk.LEFT, padx=5)


computer_choice_label = tk.Label(window, text="", bg='#f0f0f0')
computer_choice_label.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 14), bg='#f0f0f0')
result_label.pack(pady=10)

score_label = tk.Label(window, text="Score: You 0 - 0 Computer", font=("Arial", 12), bg='#f0f0f0')
score_label.pack(pady=10)


tk.Button(window, text="Reset Game", command=reset_game, bg='red', fg='white').pack(pady=10)


scores = {'user': 0, 'computer': 0}


window.mainloop()
