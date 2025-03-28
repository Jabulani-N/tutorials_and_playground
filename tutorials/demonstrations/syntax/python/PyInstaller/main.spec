# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'], # entry point of the python script
    pathex=[],
    binaries=[],
    # datas are additional files the entry point needs access to, like helper function files
    datas=[('*.py','.')], # ('target_file','target_file_location')
    hiddenimports=[
        'numpy', # needed python modules go in this list
    ],
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
    name='filename.exe', # name of the created exe
    author='Jabulani Ndhlovu', # author name~
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
    icon='D:\Temp\Stable Diffusion outputs\\00413 - face with gleam.png', # explicit address
    version='version.rc', # rc file holding version info
)
