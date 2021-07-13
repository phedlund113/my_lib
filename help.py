#-------------------------------------------------------------------------------
# Name:        Help.py
# Purpose:
#
# Author:      USPEHED
#
# Created:     25/07/2018
# Copyright:   (c) USPEHED 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#
# pylint: disable=unused-wildcard-import, method-hidden
#

"""Reads a text file and displays it in a toplevel window. 
    get_lib_version() Show numeric version of library.
    get_lib_full_version()  Show numeric version and library filename.
    example:
    Dialog(mainframe, title='TEST HELP', filename = 'help.demo')
"""

from tkinter import *
from tkinter import ttk

import os

name_help    = 'help.py'
version_help = '2.0.0'
date_help    = '02/05/21'
author_help  = 'Peter A. Hedlund'

LIB_NAME = name_help
LIB_VERSION = version_help
LIB_DATE = date_help
LIB_AUTHOR = author_help


def get_lib_version(): 
    """    Returns version information only. """
    return LIB_VERSION 


def get_full_lib_version():
    """Returns version information and library name.""" 
    msg = get_lib_version()
    rs = 'Library Name : ' + LIB_NAME + '\nVersion : ' + msg
    rs = rs + '\nDate : ' + LIB_DATE
    rs = rs + '\nAuthor : ' + LIB_AUTHOR + '\n' 
    return rs


class Dialog(Toplevel):
    """This is the called routine  see example below for useage. """
    def __init__(self, parent, title = None, filename = None):

        Toplevel.__init__(self, parent)
        self.transient(parent)

        if title:
            self.title(title)
        if filename == None:
            filename = 'read.me'

        self.parent = parent

        self.result = None

        body = Frame(self)
        self.initial_focus = self.body(body, filename)
        body.pack(padx=5, pady=5)

        self.buttonbox()

        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.ok)

        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))

        self.initial_focus.focus_set()

        self.wait_window(self)

    #
    # construction hooks

    def body(self, master, fn):
        # create dialog body.  return widget that should have
        # initial focus.  this method should be overridden
        txt1 = Text(master, width=60, height=34, fg='lightgreen', bg='black', padx=15, pady=15)
        txt1.grid(column=2, row=0, columnspan=6, rowspan=20, sticky="nsew")
        txt1.insert(1.0, "Help File\n")

        with open(fn, 'rb') as f:
            txt1.insert(END, f.read())

        #  Scrollbar linked to text box above
        scrollb = ttk.Scrollbar(master, command=txt1.yview)
        scrollb.grid(row=0, column=7, rowspan=20, sticky='nse')
        txt1['yscrollcommand'] = scrollb.set


    def buttonbox(self):
        # add standard button box. override if you don't want the
        # standard buttons

        box = Frame(self)

        w = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)

        box.pack()

    #
    # standard button semantics

    def ok(self, event=None):

        if not self.validate():
            self.initial_focus.focus_set() # put focus back
            return

        self.withdraw()
        self.update_idletasks()

        self.apply()
        self.parent.focus_set()
        self.destroy()


    #
    # command hooks

    def validate(self):

        return 1 # override

    def apply(self):

        pass # override



if __name__ == "__main__":
    from tkinter import *
    from tkinter import ttk

    def call_help():
        Dialog(mainframe, title='TEST HELP', filename = 'help.demo')

    prog_id = {'progname': 'help.py',
               'title': 'help box',
               'version': '1.0',
               'date': "31 July 2018",
               'rev_date': '',
               'author': "Peter Hedlund",
               'description': 'Stand alone test of help box.\n'
              }

    root = Tk()
    #  prevent window resizing.
    root.resizable(0, 0)
    # Replace tk icon with your own.
    root.title(prog_id['title'])

    mainframe = ttk.Frame(root, padding="3", height=100, width=300)
    mainframe.grid(column=1, row=2, sticky=(N, W, E, S))
    mainframe.grid_propagate(0)
    mainframe.tk.call('tk', 'scaling', 1.2)

    btn = ttk.Button(root, text='Help Me', command=call_help)
    btn.grid(column=1, row=0)
    s = 'Filename : Version [' + get_full_lib_version() + ']\n'
    lab2 = Label(mainframe,text=s)
    lab2.grid(column=0,row=3, columnspan=2)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()


