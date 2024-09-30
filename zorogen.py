import random
import string
import customtkinter as ctk
from tkinter import messagebox

# A list of random words
word_list = [
    "sunshine", "ocean", "mountain", "river", "forest", "desert", "moonlight", 
    "breeze", "thunder", "storm", "snowflake", "rainbow", "galaxy", "comet", 
    "starlight", "planet", "volcano", "tiger", "elephant", "dolphin", "whale", 
    "wolf", "butterfly", "eagle", "panda", "zebra", "sunflower", "rose", "daisy", 
    "tulip", "violet", "orchid", "lily", "magnolia", "clover", "maple", "cedar", 
    "pine", "willow", "bamboo", "oak", "sand", "rock", "pebble", "hill", "cloud", 
    "wind", "wave", "current", "field", "meadow"
]

# Function to generate a more secure password
def generate_secure_password(total_length, include_numbers, include_symbols, include_uppercase):
    selected_words = []
    current_length = 0
    
    # Select random words and truncate if needed
    while current_length < total_length:
        word = random.choice(word_list)
        remaining_length = total_length - current_length
        truncated_word = word[:remaining_length]
        selected_words.append(truncated_word)
        current_length += len(truncated_word)

    # Add numbers and symbols if required
    separators = []
    if include_numbers:
        separators.append(random.choice(string.digits))
    if include_symbols:
        separators.append(random.choice(string.punctuation))

    # Build the password with numbers, symbols, and words
    password = selected_words[0]
    for word in selected_words[1:]:
        if separators:
            password += random.choice(separators)
        password += word

    # Add at least one uppercase letter if required
    if include_uppercase:
        uppercase_position = random.randint(0, len(password) - 1)
        password = password[:uppercase_position] + password[uppercase_position].upper() + password[uppercase_position + 1:]

    # Shuffle the characters to avoid patterns
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

# Function to handle password generation from GUI inputs
def on_generate_password():
    try:
        total_length = int(entry_length.get())
        if total_length < 12:
            ctk.messagebox.showwarning("Warning", "For better security, consider a password length of at least 12 characters.")
        if total_length < 4:
            ctk.messagebox.showerror("Error", "Password length should be at least 4 characters.")
            return
    except ValueError:
        ctk.messagebox.showerror("Error", "Please enter a valid number for the password length.")
        return

    include_numbers = var_numbers.get()
    include_symbols = var_symbols.get()
    include_uppercase = var_uppercase.get()

    password = generate_secure_password(total_length, include_numbers, include_symbols, include_uppercase)
    label_result.config(text=f"Generated Password: {password}")

# Initialize the custom tkinter window
ctk.set_appearance_mode("Dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = ctk.CTk()
root.title("Secure Password Generator")

# GUI Layout
label_intro = ctk.CTkLabel(root, text="Enter your desired password options below:", font=('Arial', 12))
label_intro.pack(pady=10)

# Input for password length
frame_length = ctk.CTkFrame(root)
label_length = ctk.CTkLabel(frame_length, text="Password Length:", font=('Arial', 10))
label_length.pack(side=ctk.LEFT, padx=5)
entry_length = ctk.CTkEntry(frame_length, width=120)
entry_length.pack(side=ctk.LEFT, padx=5)
frame_length.pack(pady=10)

# Checkboxes for options (numbers, symbols, uppercase letters)
frame_options = ctk.CTkFrame(root)
var_numbers = ctk.BooleanVar()
var_symbols = ctk.BooleanVar()
var_uppercase = ctk.BooleanVar()

check_numbers = ctk.CTkCheckBox(frame_options, text="Include Numbers", variable=var_numbers)
check_symbols = ctk.CTkCheckBox(frame_options, text="Include Symbols", variable=var_symbols)
check_uppercase = ctk.CTkCheckBox(frame_options, text="Include Uppercase Letters", variable=var_uppercase)

check_numbers.pack(side=ctk.LEFT, padx=10)
check_symbols.pack(side=ctk.LEFT, padx=10)
check_uppercase.pack(side=ctk.LEFT, padx=10)
frame_options.pack(pady=10)

# Button to generate password
btn_generate = ctk.CTkButton(root, text="Generate Secure Password", command=on_generate_password, font=('Arial', 10))
btn_generate.pack(pady=20)

# Label to display the generated password
label_result = ctk.CTkLabel(root, text="", font=('Arial', 12, 'bold'))
label_result.pack(pady=10)

# Start the GUI event loop
root.mainloop()
