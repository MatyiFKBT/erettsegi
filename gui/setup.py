from cx_Freeze import setup, Executable
import os
os.environ['TCL_LIBRARY'] = "C:\\Users\\matol\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\matol\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"

base = None    

executables = [Executable("erettsegi_downloader.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Éreccségi",
    options = options,
    version = "1",
    description = 'nincs gond',
    executables = executables
)
