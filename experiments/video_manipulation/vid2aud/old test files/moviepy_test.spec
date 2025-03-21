# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['import_moviepy.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'moviepy',
        'numpy',
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
    name='moviepy_test.exe',
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
