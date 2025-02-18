#!/usr/bin/env python3
"""
prompts user to select a folder
returns address of selected folder
"""

import tkinter as tk
from tkinter import filedialog

def select_stage(dialogue_box_text="Please select a directory"):
    """
    opens window for user to select a folder
    """

    # Create a hidden root window
    root = tk.Tk()
    # Hide the root window
    root.withdraw()

    # Prompt the user to select a folder
    dirloc = filedialog.askdirectory(title=dialogue_box_text)

    print(f"Selected folder: {dirloc}")
    return dirloc

if __name__ == '__main__':
    select_stage()
