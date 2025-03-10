import re
import tkinter as tk
from tkinter import messagebox

# Password assessment logic
def assess_password_strength(password):
    strength_points = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength_points += 1
    else:
        feedback.append("❗ Password should be at least 8 characters long.")

    # Uppercase letter check
    if re.search(r'[A-Z]', password):
        strength_points += 1
    else:
        feedback.append("❗ Add at least one uppercase letter (A-Z).")

    # Lowercase letter check
    if re.search(r'[a-z]', password):
        strength_points += 1
    else:
        feedback.append("❗ Add at least one lowercase letter (a-z).")

    # Digit check
    if re.search(r'[0-9]', password):
        strength_points += 1
    else:
        feedback.append("❗ Add at least one number (0-9).")

    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_points += 1
    else:
        feedback.append("❗ Add at least one special character (e.g., @, #, $, %, etc.).")

    # Strength evaluation
    if strength_points == 5:
        strength = "🔒 Very Strong"
    elif strength_points == 4:
        strength = "✅ Strong"
    elif strength_points == 3:
        strength = "⚠️ Moderate"
    else:
        strength = "❌ Weak"

    return strength, feedback

# Function to handle button click
def check_password():
    password = entry_password.get()

    if not password:
        messagebox.showwarning("Input Error", "Please enter a password!")
        return

    strength, feedback = assess_password_strength(password)

    # Update the result label
    label_result.config(text=f"Password Strength: {strength}")

    # Clear previous feedback
    text_feedback.delete("1.0", tk.END)

    # Show suggestions
    if feedback:
        for tip in feedback:
            text_feedback.insert(tk.END, f"{tip}\n")
    else:
        text_feedback.insert(tk.END, "✅ Your password looks good!")

# Create main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.resizable(False, False)

# Styling
root.config(bg="#f0f0f0")
font_label = ("Arial", 12)
font_entry = ("Arial", 12)

# Widgets
label_title = tk.Label(root, text="🔐 Password Strength Checker", font=("Arial", 16, "bold"), bg="#f0f0f0")
label_title.pack(pady=10)

entry_password = tk.Entry(root, width=30, show="*", font=font_entry)
entry_password.pack(pady=5)

button_check = tk.Button(root, text="Check Strength", command=check_password, font=font_label, bg="#4CAF50", fg="white")
button_check.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
label_result.pack(pady=10)

text_feedback = tk.Text(root, height=6, width=45, font=("Arial", 10))
text_feedback.pack(pady=5)

# Run the GUI event loop
root.mainloop()
