#!/usr/bin/env python3

import moviepy
from moviepy import VideoFileClip
from moviepy import AudioFileClip
import os
import sys


# this may be what fixes the windows executable.
# testing first unprotected. will protect it next.
output = open("output.txt", "wt")
sys.stdout = output
sys.stderr = output


def vid_to_m4a():
    """
    most basic of video converters
    This will have the basis from which I add functionality

    This does not allow user to select file,
    because I want to establish the basics first.

    Next step will be custom file addresses
    """
    source_loc = '../../img/vid_manip/'
    save_loc = './vid_to_m4a/outputs/'
    vid_file = source_loc + 'example_vid.mp4'
    m4a_file = save_loc + 'output_audio.m4a'
    output_codec = "aac" # aac can be used in m4a files

    print("varibles declared")

    # import video as VideoFileClip
    video_clip = VideoFileClip(vid_file)
    print("video file imported as VideoFileClip without incident")
    # get audio from video
    audio_clip = video_clip.audio
    print("audio extracted from video as AudioFileClip without incident")

    # audio writing

    # ffmpeg will refuse to make a directory that doesn't already exist
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
    vid_to_m4a()
