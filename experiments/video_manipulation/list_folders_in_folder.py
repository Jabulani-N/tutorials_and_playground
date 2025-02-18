#!/usr/bin/env python3
"""
this module exists to quickly list dir within a given dir

recieves a folder address
    returns names of all subdirs
    returns a list
    returns None if no subdirs
"""


import os


def list_dirs(dir_address="./"):
    """
    this function recieves a folder address
    returns names of all dirs within
    but only one depth deep

    returns a list
    """
    subdirs = []
    try:
        for entry in os.listdir(dir_address):
            # lower() to make extensions case insensitive
            if os.path.isdir(os.path.join(dir_address, entry)):
                subdirs.append(entry)
    except FileNotFoundError:
        print("directory ", dir_address, " does not exist")
    except Exception as e:
        print("an exception occured:\n", e)

    if subdirs == []:
        print("no subdirectories found in dir ",
              dir_address)
        return None
    return subdirs

if __name__ == '__main__':
    # test mode
    print("you are running a test for list_folders!\
\nyou'll be prompted to enter a dir to seach\
\nand an extension to look for.\
\n\nGood luck!")
    dir_address = input("what directory do you want to search?")
    subdirs = list_dirs(dir_address)
    print("we looked for folders in dir ", dir_address,
          " and found:\n", subdirs)
