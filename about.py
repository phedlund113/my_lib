#
# pylint: disable=unused-wildcard-import, method-hidden
#

""" About Box
get_lib_version() Show numeric version of library.
get_lib_full_version()  Show numeric version and library filename.
about_box()  Displays data from prog_id in an about box. 
"""


from tkinter import messagebox

name_about    = 'about.py'
version_about = '2.0.0'
date_about    = '02/05/21'
author_about  = 'Peter A. Hedlund'

LIB_NAME = name_about
LIB_VERSION = version_about
LIB_DATE = date_about
LIB_AUTHOR = author_about


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


def about_box(prog_id):
    """Shows the about box filled with prog_id information. """
    messagebox.showinfo("About " + prog_id['progname'],
                          "Filename : " + prog_id['progname'] + "\n" +
                          "Title : " + prog_id['title'] + "\n" +
                          "Version : " + prog_id['version'] + "\n" +
                          "Creation Date : " + prog_id['date'] + "\n" +
                          "Revision Date : " + prog_id['rev_date'] + "\n" +
                          "Author : " + prog_id['author'] + "\n" +
                          "Description : " + prog_id['description']
                          )


if __name__ == "__main__":
    from tkinter import *
    from tkinter import ttk

    def my_about_box(none):
        about_box(prog_id)

    prog_id = {'progname': 'about.py',
               'title': 'Test About Box',
               'version': '1.1',
               'date': "1 February 2018",
               'rev_date': '',
               'author': "Peter Hedlund",
               'description': 'Stand alone test of about box.\n'
              }

    root = Tk()
    #  prevent window resizing.
    root.resizable(0, 0)
    # Replace tk icon with your own.
    root.title(prog_id['title'])

    mainframe = ttk.Frame(root, padding="3", height=100, width=300)
    mainframe.grid(column=1, row=2, sticky=(N, W, E, S))
    mainframe.grid_propagate(0)

    lab = Label(mainframe, text="About", relief=SUNKEN, anchor='center', width=13, bg='#ccffcc')
    lab.grid(column=1, row=0, padx=15, pady=5)
    lab.bind("<Button-1>", my_about_box)

    s = 'Filename : Version [' + get_full_lib_version() + ']\n'
    lab2 = Label(mainframe,text=s)
    lab2.grid(column=0,row=1, columnspan=2)
    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()
