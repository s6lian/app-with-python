# app-with-python

Here is an small app created by python.

- The main libraries used: sqlite3 and tkinter
  sqlite3 is used for database connection and manipulation
  tkinter is uesed for GUI

- To convert the .py to .app, the pyinstaller package is installed.
  During this process, I fixed the .exe crash problem which is related to Tk/Tcl files not being successfully copied by Pyinstaller.

- Here are some hints for the .exe crash:
  OS: High Sierra 10.13.2,  Python:3.6.3    
  Pyinstaller:3.3.1 (manually install from https://pypi.python.org/pypi/PyInstaller/3.3.1)
  
  Edit the Pyinstaller/Hooks/hook-_tkinter.py and loader/rthooks/pyi_rth__tkinter.py. Renaming the Tcl/Tk resource folders on these folders to "TclResources" and "TkResources". See details in https://github.com/pyinstaller/pyinstaller/pull/2969/files
  
  Reference(https://github.com/pyinstaller/pyinstaller/pull/2969
  https://github.com/pyinstaller/pyinstaller/pull/3132)
  
  Then use commands to install pyinstaller
    cd bootloader
    python ./waf distclean all
    python setup.py install
    
  Then build up app with pyinstaller: pyinstaller --onefile --windowed frontend.py
  
  
