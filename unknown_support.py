#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Mar 30, 2020 03:24:11 PM IST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global che61
    che61 = tk.IntVar()
    global che62
    che62 = tk.IntVar()
    global che63
    che63 = tk.IntVar()
    global che44
    che44 = tk.IntVar()
    global che45
    che45 = tk.IntVar()
    global che46
    che46 = tk.IntVar()
    global che47
    che47 = tk.IntVar()
    global che48
    che48 = tk.IntVar()
    global threshold_value
    threshold_value = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def detect():
    print('unknown_support.detect')
    sys.stdout.flush()

def next_image():
    print('unknown_support.next_image')
    sys.stdout.flush()

def open_folder():
    print('unknown_support.open_folder')
    sys.stdout.flush()

def prev_image():
    print('unknown_support.prev_image')
    sys.stdout.flush()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import unknown
    unknown.vp_start_gui()




