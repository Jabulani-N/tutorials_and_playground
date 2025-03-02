# -*- mode: python ; coding: utf-8 -*-

import os

requirements_file = "requirements.txt"
if os.path.exists(requirements_file):
    with open(requirements_file, "r") as f:
        hidden_imports = [line.strip().split("==")[0] for line in f if line.strip()]
else:
    hidden_imports = []


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('*.py','.')], # all local files with relevant modules are in folder "."
    hiddenimports=[
        'numpy',
        'moviepy',
        'pathlib',
        'os',
        'sys',
        'tkinter'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='vid2aud.exe',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # only windows and mac can use icon
    icon='D:\Temp\Stable Diffusion outputs\\00413 - face with gleam.png',
)

# coll = COLLECT( # this will put the produced result in a folder
#     exe,
#     a.binaries,
#     a.zipfiles,
#     a.datas,
#     strip=False,
#     upx=True,
#     upx_exclude=[],
#     name='vid2aud-coll', # name of the folder
#     distpath='../vid2aud/', # location of the folder?
# )
