import tkinter as tk
from customtkinter import *

### Asset Tracking System v1.1

### Creating a login message as a Function
def display_login_message():
    return """\nWelcome to the ISMS Asset Tracking System v1.\n
Warning, Unauthorized Access is Prohibited with severe penalties. By logging into the system, you are legally responsible."""

## define tkinter application 
root = tk.Tk()
root.title("Asset Tracking System v1.1")

### tkinter resources
login_message_label = CTkLabel(root, text=display_login_message())
login_message_label.pack(padx=2, pady=2)

# Username Entry
username_label = CTkLabel(root, text="Username:")
username_label.pack()
username_entry = CTkEntry(root)
username_entry.pack()

# Password Entry
password_label = CTkLabel(root, text="Password:")
password_label.pack()
password_entry = CTkEntry(root)
password_entry.pack()

# Login button
login_button = CTkButton(root, text="Login")
login_button.pack(pady=10)

## launch tkinter application 
root.mainloop()
