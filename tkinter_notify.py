"""
Tkinter solution to displaying text on error in GUI program.

Usage: notify(title='Test', message='Test message')
"""

try:
    # try importing python3 version first
    from Tkinter import Tk
    import tkMessageBox as messagebox
except ImportError:
    # if that failed, try python2 version
    from tkinter import Tk, messagebox

def notify(title='', message=''):
    Tk().withdraw()
    messagebox.showinfo(title=title, message=message) 

if __name__ == '__main__':
    msg = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    notify('Lorem Ipsum', msg)
