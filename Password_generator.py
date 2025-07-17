import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    password_var.set(password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.configure(bg="#f3e5f5")

tk.Label(root, text="Enter password length:", font=("Arial", 12, "bold"), bg="#f3e5f5", fg="#6a1b9a").pack(pady=10)
length_entry = tk.Entry(root, font=("Arial", 12), width=10, justify='center')
length_entry.pack(pady=5)

tk.Button(root, text="Generate Password", font=("Arial", 12, "bold"), bg="#ce93d8", fg="#4a148c",
          command=generate_password).pack(pady=10)

password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 14), width=30, justify='center', state='readonly', bg="#fffde7")
password_entry.pack(pady=10)

tk.Button(root, text="Copy to Clipboard", font=("Arial", 12, "bold"), bg="#81d4fa", fg="#01579b",
          command=copy_password).pack(pady=10)

root.mainloop()