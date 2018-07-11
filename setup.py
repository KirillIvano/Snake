from cx_Freeze import setup, Executable
import os

base = "Win32GUI"
executables = [Executable("Activate.py", base=base)]
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
packages = ["idna"]
options = {
    'build_exe': {

        'packages': packages,'include_files':['images', 'util_files', 'sounds', 'music',]
    }, }

setup(
    name="<any name>",
    options=options,
    version="1.0",
    description='<any description>',
    executables=executables
)