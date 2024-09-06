import hashlib
import tkinter as tk
from tkinter import messagebox

# Function to hash the password using SHA-256
def hash_password():
    password = password_entry.get()  # Get password from the entry box
    if not password:
        messagebox.showerror("Input Error", "Please enter a password!")
        return
    
    # Hash the password with SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Display the hashed password in the result entry
    result_entry.delete(0, tk.END)  # Clear the entry before showing the result
    result_entry.insert(0, hashed_password)

# Function to clear all inputs
def clear_inputs():
    password_entry.delete(0, tk.END)
    result_entry.delete(0, tk.END)

# Creating the main window
root = tk.Tk()
root.title("Password Hasher - SHA-256")

# Setting window size
root.geometry("400x200")

# Adding password label and entry
password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=5)

password_entry = tk.Entry(root, width=40, show="*")
password_entry.pack(pady=5)

# Adding a button to hash the password
hash_button = tk.Button(root, text="Hash Password", command=hash_password)
hash_button.pack(pady=10)

# Adding result label and entry (readonly to display the hash)
result_label = tk.Label(root, text="Hashed Password (SHA-256):")
result_label.pack(pady=5)

result_entry = tk.Entry(root, width=40)
result_entry.pack(pady=5)

# Adding a button to clear inputs
clear_button = tk.Button(root, text="Clear", command=clear_inputs)
clear_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
