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
def ask_two_options(opt1="1", opt2="2",box_title="Choose an Option",
                    box_text = "Please select one of the following options:"):
    # Create a new top-level window for the dialog
    dialog = tk.Toplevel(root)
    dialog.title(box_title)
    dialog.geometry("600x250")
    dialog.resizable(False, False)

    # Variable to store the user's choice
    user_choice = tk.StringVar(value="Cancel")  # Default to "Cancel"

    # Label with the message
    tk.Label(dialog, text=box_text).pack(pady=10)

    # Buttons for the three options
    def select_option(option):
        user_choice.set(option)
        dialog.destroy()  # Close the dialog

    tk.Button(dialog, text=opt1, command=lambda: select_option(opt1)).pack(pady=5)
    tk.Button(dialog, text=opt2, command=lambda: select_option(opt2)).pack(pady=5)
    tk.Button(dialog, text="Cancel", command=lambda: select_option("cancel")).pack(pady=5)

    # Wait for the user to make a selection
    dialog.wait_window()

    return user_choice.get()


if __name__ == '__main__':
    # Call the function and store the result
    selected_option = ask_two_options()
    print(f"You selected: {selected_option}")
