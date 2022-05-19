# coding=utf8
#launch from cmd: python setup.py build
     
from cx_Freeze import setup, Executable

target = Executable(
    script="red.py",
    #base="Win32GUI",
    icon="64x64.ico"
    )

setup(
    name="RED MANAGE",
    version="1.1.1",
    description="Network cleaning software",
    author="Alenga",
    executables=[target]
    )