# How to fix PyInstaller failing to transfer the package metadata when creating an executable

`importlib.metadata.PackageNotFoundError: No package metadata was found for imageio
[PYI-25132:ERROR] Failed to execute script 'main' due to unhandled exception!`


![moveipy error](../../../../img/tutorials/quick%20fixes/moviepy%20error%20with%20imageio%20b.PNG)
If when trying to run the executable from a python script that imports MoviePy, it returns the Terminal error `line 19, in <module>
    import moviepy` ...  `importlib.metadata.PackageNotFoundError: No package metadata was found for imageio`, you can solve this in your `.spec` file by putting `from PyInstaller.utils.hooks import copy_metadata` at the top of the file (below the `# -*- mode: python ; coding: utf-8 -*-`,) and append `copy_metadata('imageio')` (this returns a list of tuples) to your `datas=` line. for example, mine looks like this:

![datas to make moviepy work](../../../../img/tutorials/quick%20fixes/datas%20for%20moviepy%20pyinstaller%20import%20fix.PNG)

