import tkinter as tk
from tkinter import messagebox, filedialog
from zxcvbn import zxcvbn
import itertools
import os

# ------------ Password Analyzer ------------
def analyze_password():
    password = password_entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password")
        return

    result = zxcvbn(password)
    score = int(result["score"] * 2.5)  # Convert 0–4 scale to 0–10

    feedback = result["feedback"]
    feedback_text = f"Score (0-10): {score}\n"
    feedback_text += f"Guesses: {result['guesses']}\n"
    feedback_text += f"Crack Time: {result['crack_times_display']['offline_fast_hashing_1e10_per_second']}\n"
    feedback_text += f"Feedback: {feedback}"

    messagebox.showinfo("Password Analysis", feedback_text)


# ------------ Wordlist Generator ------------
def generate_wordlist():
    name = name_entry.get()
    nickname = nickname_entry.get()
    parent = parent_entry.get()
    yob = yob_entry.get()

    if not (name or nickname or parent or yob):
        messagebox.showwarning("Input Error", "Please enter at least one detail")
        return

    words = set([name, nickname, parent, yob])
    words = {w for w in words if w}  # Remove empty strings

    wordlist = set(words)

    # Leetspeak variations
    leet_map = {"a": "@", "s": "$", "o": "0", "i": "1", "e": "3"}
    for word in words:
        for char, leet in leet_map.items():
            if char in word.lower():
                wordlist.add(word.lower().replace(char, leet))

    # Combine words
    for combo in itertools.permutations(words, 2):
        wordlist.add("".join(combo))

    # Add years (if yob is valid)
    if yob.isdigit():
        year = int(yob)
        for i in range(year, year + 5):  # Example: 2001–2005
            wordlist.update([f"{name}{i}", f"{nickname}{i}", f"{parent}{i}"])

    # Save to file
    os.makedirs("wordlist", exist_ok=True)
    save_path = filedialog.asksaveasfilename(
        defaultextension=".txt", initialdir="wordlist", title="Save Wordlist"
    )

    if save_path:
        with open(save_path, "w") as f:
            for word in sorted(wordlist):
                f.write(word + "\n")
        messagebox.showinfo("Wordlist Generated", f"Saved {len(wordlist)} entries at:\n{save_path}")


# ------------ GUI Layout ------------
root = tk.Tk()
root.title("Password Analyzer & Wordlist Generator")
root.geometry("500x400")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="🔐 Password Strength Analyzer", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Password Analyzer Section
frame1 = tk.LabelFrame(root, text="Password Strength Analyzer", padx=10, pady=10)
frame1.pack(padx=10, pady=10, fill="x")

password_label = tk.Label(frame1, text="Enter Password:")
password_label.pack(anchor="w")
password_entry = tk.Entry(frame1, width=40, show="*")
password_entry.pack(anchor="w", pady=5)

analyze_button = tk.Button(frame1, text="Analyze Password", command=analyze_password)
analyze_button.pack(pady=5)

# Wordlist Generator Section
frame2 = tk.LabelFrame(root, text="Custom Wordlist Generator", padx=10, pady=10)
frame2.pack(padx=10, pady=10, fill="x")

name_label = tk.Label(frame2, text="Name:")
name_label.grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(frame2, width=25)
name_entry.grid(row=0, column=1)

nickname_label = tk.Label(frame2, text="Nickname:")
nickname_label.grid(row=1, column=0, sticky="w")
nickname_entry = tk.Entry(frame2, width=25)
nickname_entry.grid(row=1, column=1)

parent_label = tk.Label(frame2, text="Parent’s Name:")
parent_label.grid(row=2, column=0, sticky="w")
parent_entry = tk.Entry(frame2, width=25)
parent_entry.grid(row=2, column=1)

yob_label = tk.Label(frame2, text="Year of Birth:")
yob_label.grid(row=3, column=0, sticky="w")
yob_entry = tk.Entry(frame2, width=25)
yob_entry.grid(row=3, column=1)

wordlist_button = tk.Button(frame2, text="Generate Wordlist", command=generate_wordlist)
wordlist_button.grid(row=4, columnspan=2, pady=10)

# Run App
root.mainloop()
