import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")
root.configure(bg="#87ceeb")  # Sky blue background

label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14, "bold"), bg="#87ceeb")
label.pack(pady=20)

button_frame = tk.Frame(root, bg="#87ceeb")
button_frame.pack(pady=10)

for choice in ["rock", "paper", "scissors"]:
    btn = tk.Button(button_frame, text=choice.capitalize(), width=10, height=2, font=("Arial", 12, "bold"),
                    bg="#ffd1dc", fg="#333", command=lambda c=choice: play_game(c))
    btn.pack(side=tk.LEFT, padx=10)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#87ceeb")
result_label.pack(pady=10)

# Add Exit button (move upward by reducing pady)
exit_button = tk.Button(root, text="Exit", command=root.destroy, width=6, height=1, font=("Arial", 10, "bold"), bg="#ff6666", fg="#fff")
exit_button.pack(pady=2)

root.mainloop()

