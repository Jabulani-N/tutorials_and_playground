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

### Baseline functionality

 - [x] import video file

 - [x] isolate audio data

 - [x] save audio data as alternate file

### Future-proofing functionality

 - [x] video file name can be specified as input argument
        * took a two argument route. can have the function that feeds it files handle name duplication
   - [ ] created audio file inherits name of video it came from
        * despite wording, this can just copy the input argument and modify it a little
        * this means I can make a wholly separate `nameconverter(video_name, desired_extension)` function that converts a video name to one with the `desired_extension`.
        * This funciotnality will come from the function that spams feeding names to the main converter

 - [ ] independant function that returns the names of all video files in a given directory
    * this will feed the filenames to the previous task of converting videos based on filename as input argument.

## efficiency functionality

 - [ ] skip importing video files that already have existing audio file
   - [ ] make this optional so files can be updated

## Resources

MoviePy can [directly such the audio out of a videoClip](https://zulko.github.io/moviepy/reference/reference/moviepy.video.VideoClip.VideoClip.html#moviepy.video.VideoClip.VideoClip.audio) via `moviepy.video.VideoClip.VideoClip.audio()` This will return a MoviePy AudioClip object. This should mean as soon as we get a VideoClip object, we can just truncate it and use `extracted_audio = VideoClipName.audio` to instantly grab the AudioClip equivalent of the file.

[This is how you get a videofileclip out of a video file](https://zulko.github.io/moviepy/user_guide/loading.html#videofileclip) All we need is `myclip = VideoFileClip("example.mp4")`, which makes a VideoFileClip object named `myclip`,but the link will explain how to only take portions off a video.

## Programmers' Potential Pitfalls

VideoClip is distinct form VideoFileClip. Same with audio.

`extracted_audio = VideoClipName.audio()` will fail, raising `TypeError: 'AudioFileClip' object is not callable`

* instead use `extracted_audio = VideoClipName.audio`
