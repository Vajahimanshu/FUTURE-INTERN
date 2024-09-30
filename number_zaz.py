import random
import tkinter as tk
from tkinter import messagebox
import time

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Number Guessing Game")
        self.root.geometry("500x400")
        self.root.config(bg="#e0e0e0")
        
        # Initialize variables
        self.number_to_guess = None
        self.guess_count = 0
        self.max_attempts = None
        self.start_time = None
        self.difficulty = None
        self.game_active = False
        
        # Game statistics
        self.wins = 0
        self.losses = 0
        self.total_guesses = 0
        
        # Difficulty levels
        self.difficulty_options = {
            "Easy": (1, 50, 10),
            "Medium": (1, 100, 7),
            "Hard": (1, 500, 5)
        }
        
        # Create GUI elements
        self.heading = tk.Label(root, text="Advanced Number Guessing Game", font=("Arial", 16, "bold"), bg="#e0e0e0")
        self.heading.pack(pady=10)
        
        self.label = tk.Label(root, text="Choose Difficulty Level:", font=("Arial", 12), bg="#e0e0e0")
        self.label.pack(pady=10)
        
        self.difficulty_var = tk.StringVar(value="Easy")
        self.difficulty_menu = tk.OptionMenu(root, self.difficulty_var, *self.difficulty_options.keys())
        self.difficulty_menu.config(font=("Arial", 12))
        self.difficulty_menu.pack(pady=5)
        
        self.start_button = tk.Button(root, text="Start Game", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.start_game)
        self.start_button.pack(pady=10)
        
        self.entry = tk.Entry(root, font=("Arial", 12), justify="center", width=10, state='disabled')
        self.entry.pack(pady=5)
        
        self.guess_button = tk.Button(root, text="Submit Guess", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.check_guess, state='disabled')
        self.guess_button.pack(pady=10)
        
        self.hint_label = tk.Label(root, text="", font=("Arial", 12, "italic"), bg="#e0e0e0", fg="#333")
        self.hint_label.pack(pady=5)
        
        self.stats_label = tk.Label(root, text="Wins: 0 | Losses: 0 | Total Guesses: 0", font=("Arial", 12), bg="#e0e0e0", fg="#333")
        self.stats_label.pack(pady=10)
        
        self.time_label = tk.Label(root, text="Time taken: 0 seconds", font=("Arial", 12), bg="#e0e0e0", fg="#333")
        self.time_label.pack(pady=10)
        
        self.reset_button = tk.Button(root, text="Reset Game", font=("Arial", 12), bg="#f44336", fg="white", command=self.reset_game, state='disabled')
        self.reset_button.pack(pady=5)
    
    def start_game(self):
        self.difficulty = self.difficulty_var.get()
        num_range, self.max_attempts, _ = self.difficulty_options[self.difficulty]
        self.number_to_guess = random.randint(1, num_range)
        self.guess_count = 0
        self.game_active = True
        self.start_time = time.time()
        
        self.entry.config(state='normal')
        self.guess_button.config(state='normal')
        self.reset_button.config(state='normal')
        
        self.hint_label.config(text=f"Guess a number between {self.difficulty_options[self.difficulty][0]} and {self.difficulty_options[self.difficulty][1]}")
        self.update_time()
    
    def check_guess(self):
        try:
            user_guess = int(self.entry.get())
            num_range, _, _ = self.difficulty_options[self.difficulty]
            if user_guess < 1 or user_guess > num_range:
                raise ValueError("Out of bounds")
            
            self.guess_count += 1
            self.total_guesses += 1
            
            if user_guess > self.number_to_guess:
                self.hint_label.config(text="Too high! Try again.", fg="#D32F2F")
            elif user_guess < self.number_to_guess:
                self.hint_label.config(text="Too low! Try again.", fg="#1976D2")
            else:
                self.hint_label.config(text="", fg="#333")
                self.end_game(True)
                return
            
            if self.guess_count >= self.max_attempts:
                self.end_game(False)
            else:
                self.entry.delete(0, tk.END)
        
        except ValueError:
            messagebox.showwarning("Invalid input", "Please enter a valid number.")
            self.entry.delete(0, tk.END)
    
    def end_game(self, won):
        self.game_active = False
        self.entry.config(state='disabled')
        self.guess_button.config(state='disabled')
        
        time_taken = int(time.time() - self.start_time)
        self.time_label.config(text=f"Time taken: {time_taken} seconds")
        
        if won:
            self.wins += 1
            messagebox.showinfo("Congratulations!", f"You've guessed the number in {self.guess_count} attempts!")
        else:
            self.losses += 1
            messagebox.showinfo("Game Over", f"You've used all {self.max_attempts} attempts! The number was {self.number_to_guess}.")
        
        self.update_stats()
    
    def reset_game(self):
        self.game_active = False
        self.entry.delete(0, tk.END)
        self.entry.config(state='disabled')
        self.guess_button.config(state='disabled')
        self.reset_button.config(state='disabled')
        self.hint_label.config(text="")
        self.time_label.config(text="Time taken: 0 seconds")
    
    def update_stats(self):
        self.stats_label.config(text=f"Wins: {self.wins} | Losses: {self.losses} | Total Guesses: {self.total_guesses}")
    
    def update_time(self):
        if self.game_active:
            elapsed_time = int(time.time() - self.start_time)
            self.time_label.config(text=f"Time taken: {elapsed_time} seconds")
            self.root.after(1000, self.update_time)

# Run the GUI application
root = tk.Tk()
game = GuessingGame(root)
root.mainloop()
