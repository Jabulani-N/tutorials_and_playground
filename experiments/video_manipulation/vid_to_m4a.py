#!/usr/bin/env python3

import moviepy
from moviepy import VideoFileClip



def vid_to_m4a():
    """
    most basic of video converters
    This will have the basis from which I add functionality
    """
    source_loc = '../../img/vid_manip/'
    save_loc = './vid_to_m4a/outputs/'
    vid_file = source_loc + 'example_vid.mp4'
    m4a_file = save_loc + 'output_sound.m4a'


    # Extract audio
    audio_import_bufferSize = 1000
    sound_file = moviepy.audio.io.readers.FFMPEG_AudioReader(vid_file, audio_import_bufferSize)
    # write it to the specified location
    fps, nbytes, output_buffersize = 25, 2, 500
    moviepy.audio.io.ffmpeg_audiowriter.ffmpeg_audiowrite(sound_file, m4a_file, fps,
                                                          nbytes, output_buffersize)

    # Close the clip
    sound_file.close()


def vid_to_m4a_old():
    """
    OUTDATED
    """
    source_loc = '../../img/vid_manip/'
    save_loc = './vid_to_m4a/outputs/'
    vid_file = source_loc + 'example_vid.mp4'
    m4a_file = save_loc + 'output_sound.m4a'

    # Load the video file
    vid_clip = VideoFileClip(vid_file)

    # Extract audio and write it to the specified location
    vid_clip.audio.write_audiofile(m4a_file)

    # Close the video clip
    vid_clip.close()

