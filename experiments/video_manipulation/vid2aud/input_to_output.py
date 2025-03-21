#!/usr/bin/env python3
"""
this module puts together previously created scripts
to automatically take exposed vids in inputs dir
and convert them to outputs dir

to make this work for layered dirs later,
it has a field to tell it which dir you want it to search
    It defaults to
    input: inputs dir
    output: outputs dir
"""

import numpy as np
from pathlib import Path

list_files = __import__('list_files_in_folder').list_files
converter = __import__('named_vid_to_m4a').named_vid_to_m4a
list_subdirs = __import__('list_folders_in_folder').list_dirs


def extract_from_dir(input_dir="./input/", output_dir="./output/"):
    """
    give it a dir, and it'll loop through each vid file within
    and put it in the designated or default output dir
    you could even put them in the source dir if you want
    """
    types_of_vid = [".mp4"]
    target_vid_titles = np.array([])
    subdirs = list_subdirs(input_dir)

    # if there are subdirs, do them first
    if subdirs:
        for subdir in subdirs:
            input_subdir = input_dir + subdir + "/"
            output_subdir = output_dir + subdir + "/"
            extract_from_dir(input_subdir, output_subdir)

    for vid_type in types_of_vid:
        print("about to add files of extension", vid_type)
        target_vid_titles = np.append(target_vid_titles,(list_files(input_dir, vid_type)))
        print("just added files of extension", vid_type)

    target_vid_titles = target_vid_titles.flatten()
    print("all vid types collected.\ntotal list of vids:", target_vid_titles)

    for vid_name_full in target_vid_titles:
        vid_name_stem = Path(vid_name_full).stem
        output_aud_file_name = vid_name_stem + ".m4a"
        print("sending '", vid_name_full, "' in '", input_dir, "' to converter")
        print("to ask converter to make '", output_aud_file_name, "' in", output_dir)
        print("type of vid name full is", type(vid_name_full))
        converter(vid_name_full, output_aud_file_name, input_dir, output_dir)

if __name__ == '__main__':
    """runs the converter for vid to m4a conversion"""
    extract_from_dir()
