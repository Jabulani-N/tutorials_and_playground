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

    this module sends subdirs of selected dir to the dir converter
        it sends the output dir to be the same as the subfolder's name
"""