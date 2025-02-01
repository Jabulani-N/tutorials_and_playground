# Video Manipulation

This directory contains experimental scripts created for the purpose of batch altering/converting video files.

I created this because I wanted to convert about a hundred video files I had on hand to m4a audio format, <details>
<summary>but...</summary>


![why1a](../../img/vid_manip/monthly%20sub.PNG)

![why1b](../../img/vid_manip/one%20day%20trial.PNG)

![Fine, I'll do it myself](../../img/thanos_fine_ill_do_it_myself.png)
</details>

moviepy updated to v2, so much old guides will not function. This'll be a project filled with [reading the documentation](https://zulko.github.io/moviepy/reference/reference/moviepy.audio.AudioClip.AudioClip.html#moviepy.audio.AudioClip.AudioClip.write_audiofile).

## Steps

import video file

isolate audio data

save audio data as alternate file

## Resources

MoviePy can [directly such the audio out of a videoClip](https://zulko.github.io/moviepy/reference/reference/moviepy.video.VideoClip.VideoClip.html#moviepy.video.VideoClip.VideoClip.audio) via `moviepy.video.VideoClip.VideoClip.audio()` This will return a MoviePy AudioClip object. This should mean as soon as we get a VideoClip object, we can just truncate it and use `extracted_audio = VideoClipName.audio()` to instantly grab the AudioClip equivalent of the file.

[This is how you get a videofileclip out of a video file](https://zulko.github.io/moviepy/user_guide/loading.html#videofileclip) All we need is `myclip = VideoFileClip("example.mp4")`, which makes a VideoFileClip object named `myclip`,but the link will explain how to only take portions off a video.

## Potential Pitfalls

VideoClip is distinct form VideoFileClip. Same with audio.
