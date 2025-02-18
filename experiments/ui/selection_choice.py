#!/usr/bin/env python3
"""
prompts user to select a choice
returns selected choice
"""

import tkinter as tk
from tkinter import messagebox

# Create a hidden root window
root = tk.Tk()
# Hide the main tkinter window
root.withdraw()

# Function to display a custom dialog box with three options
def ask_three_options():
    # Create a new top-level window for the dialog
    dialog = tk.Toplevel(root)
    dialog.title("this is box title: Choose an Option")
    dialog.geometry("300x150")
    dialog.resizable(False, False)

    # Variable to store the user's choice
    user_choice = tk.StringVar(value="Cancel")  # Default to "Cancel"

    # Label with the message
    tk.Label(dialog, text="Please select one of the following options:").pack(pady=10)

    # Buttons for the three options
    def select_option(option):
        user_choice.set(option)
        dialog.destroy()  # Close the dialog

    tk.Button(dialog, text="Option one", command=lambda: select_option("Option 1")).pack(pady=5)
    tk.Button(dialog, text="Option two", command=lambda: select_option("Option 2")).pack(pady=5)
    tk.Button(dialog, text="Cancel button", command=lambda: select_option("Cancel")).pack(pady=5)

    # Wait for the user to make a selection
    dialog.wait_window()

    return user_choice.get()


if __name__ == '__main__':
    # Call the function and store the result
    selected_option = ask_three_options()
    print(f"You selected: {selected_option}")
