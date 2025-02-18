#!/usr/bin/env python3
"""
converts one mp4 video file to m4a audio,
given:

    source vid name
    source location directory
    desired output name
    output destination directory

file names required.
default directories exist, but should be specified when used.
"""

import moviepy
from moviepy import VideoFileClip
from moviepy import AudioFileClip
import os
import sys


def named_vid_to_m4a(input_vid_name, output_aud_name,
                     source_loc='../../img/vid_manip/',
                     save_loc='./vid_to_m4a/outputs/'):
    """
    phase two of video converters
    This will have the basis from which I add functionality

    This step will be custom file addresses
    This method will take target names as input args

    input args are used to this method can be called by later methods
        this is why it's NOT gonna prompt user

    This function is complete
    """

    print("converter args recieved:")
    print("input vid name:", input_vid_name)
    print("source loc:", source_loc)
    print("output aud name:", output_aud_name)
    print("save loc:", save_loc)
    vid_file = source_loc + input_vid_name
    m4a_file = save_loc + output_aud_name
    output_codec = "aac" # aac can be used in m4a files

    print("varibles declared:")
    print("source file is", vid_file, "from", source_loc)
    print("create", m4a_file, "in", save_loc)

    # import video as VideoFileClip
    video_clip = VideoFileClip(vid_file)
    print("video file imported as VideoFileClip without incident")
    # get audio from video
    audio_clip = video_clip.audio
    print("audio extracted from video as AudioFileClip without incident")

    # audio writing

    # create necessary directories
    os.makedirs(os.path.dirname(m4a_file), exist_ok=True)
    # save audio as new file
    audio_clip.write_audiofile(m4a_file, codec=output_codec)
    print("audio file written")
    # close the created clips
    video_clip.close()
    audio_clip.close()
    print("clip files closed")


if __name__ == '__main__':
    # test mode
    # running as main prompts user for vid name
    print("you are running a test for the named\
video to m4a file conversion system!\
\n\nYou'll be prompted to enter the name\
of the input file, extension included, \
and then what you want hte output file to be named.\
\n\nThis is purely funtionality for debugging.\
\nNormally, you won't actually be able to see\
this method work, as it'll be getting called internally\
and automatically.\
\n\nGood luck!\n\n  -- Jabulani Ndhlovu")
    vid_file_to_take = input("what video file will you convert?: ")
    aud_file_to_give = input("what will you name the converted file?: ")
    print("you want to take",vid_file_to_take,
          "and give audio file", aud_file_to_give)
    named_vid_to_m4a(vid_file_to_take,
                     aud_file_to_give)
