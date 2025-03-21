#!/usr/bin/env python3
"""
this is where it all comes together.

This module will create the window that asks
whether you wanna use deafult locations or select
input/output folders

it'll also handle running the converter once options have been selected
"""

converter = __import__('input_to_output').extract_from_dir
pick_from_two = __import__('pick_one_of_two').ask_two_options
pick_dir = __import__('select_dir').select_stage

def run_gui():
    # source selection
    opt1 = "use default input folder"
    opt2 = "select an input folder"
    box_title = "where are your input vids?"
    box_text = "Are your input videos in the default 'input' folder,\
\n or will you select a different folder?"
    choice = pick_from_two(opt1, opt2, box_title, box_text)
    if choice == opt1:
        source_dir = "./input"
    elif choice == opt2:
        source_dir = pick_dir("please select the folder with your videos")
    else:
        return None
    print(f"source dir = {source_dir}")
    if source_dir == None:
        return None
    if choice == "cancel":
        return None
    # output selection
    opt1 = "Create and use a default output folder right here"
    opt2 = "Select an output folder"
    box_title = "where would you like to place the audio files?"
    box_text = "Would you like to create\
 and use a default 'output' folder,\
\n or will you select a different folder to\
store the audio files after conversion?"
    choice = pick_from_two(opt1, opt2, box_title, box_text)
    if choice == opt1:
        dest_dir = "./output"
    elif choice == opt2:
        dest_dir = pick_dir("please select the\
folder where you'd like to save your audio files.")
    else:
        return None
    if choice == "cancel":
        return None

    #confirmation screen
    box_title = "Begin?"
    box_text = "We're going to take the videos out of\n" + \
source_dir + "\nand place them into\n" + dest_dir
    opt1 = "Let's go!"
    opt2 = "Start over"
    choice = pick_from_two(opt1, opt2, box_title, box_text)
    if choice == opt1:
        converter(source_dir + "/", dest_dir + "/")
    elif choice == opt2:
        run_gui()
    else:
        return

if __name__ == '__main__':
    """run the gui"""
    run_gui()
