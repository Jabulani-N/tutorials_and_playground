#!/usr/bin/env python3
"""
this module puts together previously created scripts
to automatically take exposed vids in inputs dir
and convert them to outputs dir
"""

# example module import
# determinant = __import__('0-determinant').determinant

list_files = __import__('list_files_in_folder').list_files
converter = __import__('named_vid_to_m4a').named_vid_to_m4a
