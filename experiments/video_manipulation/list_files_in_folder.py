#!/usr/bin/env python3
"""
this module exists to quickly list files with given ext in a given dir

note that you can't pass "none" as an argument and get it to work
you'll have to leave the argument slot blank in order to run it in default.

recieves a folder address
    returns names of all files with a given extension

    returns a list
"""


import os


def list_files(dir_address="./", extension=".mp4"):
    """
    this function recieves a folder address
    returns names of all files with a given extension

    returns a list
    """
    relevant_files = []
    try:
        for file in os.listdir(dir_address):
            # lower() to make extensions case insensitive
            if file.lower().endswith(extension.lower()):
                relevant_files.append(file)
    except FileNotFoundError:
        print("directory ", dir_address, " does not exist")
    except Exception as e:
        print("an exception occured:\n", e)

    if relevant_files == []:
        print("no files of extension '", extension, "' found in dir ",
              dir_address)
    return relevant_files

if __name__ == '__main__':
    # test mode
    print("you are running a test for list_files!\
\nyou'll be prompted to enter a dir to seach\
\nand an extension to look for.\
\n\nGood luck!")
    dir_address = input("what directory do you want to search?")
    extension = input("what extension do you want to search?")
    relevant_files = list_files(dir_address, extension)
    print("we looked for ", extension, " files in dir ", dir_address,
          " and found:\n", relevant_files)
