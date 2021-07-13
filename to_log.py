#
# pylint: disable=unused-wildcard-import, method-hidden
#
""" Logging functions Library 

    get_lib_version() Show numeric version of library.
    get_lib_full_version()  Show numeric version and library filename.
    to_log()  sends string to text window in last color
    to_log_red()  sends string to text window in red
    to_log_yellow()  sends string to text window in  yellow
    to_log_green()  sends string to text window in  green
    to_log_blue()  sends string to text window in  blue
    to_log_cyan()  sends string to text window in  cyan
    to_log_white()  sends string to text window in  white
    to_log_violet()  sends string to text window in  violet
    clear_log()  clears the text window
    save_log()  saves the text window to a user selected file 
"""

from tkinter import *
from tkinter import filedialog
name_to_log    = 'to_log.py'
version_to_log = '2.2.0'
date_to_log    = '04/29/21'
author_to_log  = 'Peter A. Hedlund'

LIB_NAME = name_to_log
LIB_VERSION = version_to_log
LIB_DATE = date_to_log
LIB_AUTHOR = author_to_log

# LIB_NAME = "to_log.py"
# LIB_VERSION = "2.1.0"
# LIB_DATE = '02/09/21'

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



def to_log(txt, tstr):
    """Sends string to text window. """

    txt.configure(state='normal')
    txt.insert(END, tstr)
    txt.index(END)
    txt.see(END)
    txt.update()
    txt.configure(state='disabled')


def to_log_red(txt, tstr):
    """Sends string to text window in red """
    # Enable changes to text widget
    txt.configure(state='normal')
    # position cursor at the end of the text
    txt.mark_set(INSERT, END)
    #  get starting text position
    st = txt.index('insert')
    #  Add text to text widget at the end
    txt.insert(END, tstr)
    #  get ending text position
    ed = txt.index('insert')
    # print "Start = {}  End = {}  String = {}".format(st,ed,str)   #  debug
    #  tag area bound by start and stop
    txt.tag_add("junk1", st, ed)
    #  Change color of tagged area
    txt.tag_config("junk1", foreground='red')
    #  Go to end of text window (auto scroll)
    txt.see(END)
    #  Update idle tasks
    txt.update_idletasks()
    # disable changes to text widget
    txt.configure(state='disabled')


def to_log_yellow(txt, tstr):
    """Sends string to text window in yellow """
    # Enable changes to text widget
    txt.configure(state='normal')
    # position cursor at the end of the text
    txt.mark_set(INSERT, END)
    #  get starting text position
    st = txt.index('insert')
    #  Add text to text widget at the end
    txt.insert(END, tstr)
    #  get ending text position
    ed = txt.index('insert')
    # print "Start = {}  End = {}  String = {}".format(st,ed,str)   #  debug
    #  tag area bound by start and stop
    txt.tag_add("junk2", st, ed)
    #  Change color of tagged area
    txt.tag_config("junk2", foreground='yellow')
    #  Go to end of text window (auto scroll)
    txt.see(END)
    #  Update idle tasks
    txt.update_idletasks()
    # disable changes to text widget
    txt.configure(state='disabled')


def to_log_green(txt, tstr):
    """Sends string to text window in green """
    # Enable changes to text widget
    txt.configure(state='normal')
    # position cursor at the end of the text
    txt.mark_set(INSERT, END)
    #  get starting text position
    st = txt.index('insert')
    #  Add text to text widget at the end
    txt.insert(END, tstr)
    #  get ending text position
    ed = txt.index('insert')
    # print "Start = {}  End = {}  String = {}".format(st,ed,str)   #  debug
    #  tag area bound by start and stop
    txt.tag_add("junk3", st, ed)
    #  Change color of tagged area
    txt.tag_config("junk3", foreground='green')
    #  Go to end of text window (auto scroll)
    txt.see(END)
    #  Update idle tasks
    txt.update_idletasks()
    # disable changes to text widget
    txt.configure(state='disabled')


def to_log_blue(txt, tstr):
    """Sends string to text window in blue """
    # Enable changes to text widget
    txt.configure(state='normal')
    # position cursor at the end of the text
    txt.mark_set(INSERT, END)
    #  get starting text position
    st = txt.index('insert')
    #  Add text to text widget at the end
    txt.insert(END, tstr)
    #  get ending text position
    ed = txt.index('insert')
    # print "Start = {}  End = {}  String = {}".format(st,ed,str)   #  debug
    #  tag area bound by start and stop
    txt.tag_add("junk4", st, ed)
    #  Change color of tagged area
    txt.tag_config("junk4", foreground='lightblue')
    #  Go to end of text window (auto scroll)
    txt.see(END)
    #  Update idle tasks
    txt.update_idletasks()
    # disable changes to text widget
    txt.configure(state='disabled')


def to_log_cyan(txt, tstr):
    """Sends string to text window in cyan """
    # Enable changes to text widget
    txt.configure(state='normal')
    # position cursor at the end of the text
    txt.mark_set(INSERT, END)
    #  get starting text position
    st = txt.index('insert')
    #  Add text to text widget at the end
    txt.insert(END, tstr)
    #  get ending text position
    ed = txt.index('insert')
    # print "Start = {}  End = {}  String = {}".format(st,ed,str)   #  debug
    #  tag area bound by start and stop
    txt.tag_add("junk5", st, ed)
    #  Change color of tagged area
    txt.tag_config("junk5", foreground='cyan')
    #  Go to end of text window (auto scroll)
    txt.see(END)
    #  Update idle tasks
    txt.update_idletasks()
    # disable changes to text widget
    txt.configure(state='disabled')


def to_log_white(txt, tstr):
    """Sends string to text window in white """
    # Enable changes to text widget
    txt.configure(state='normal')
    # position cursor at the end of the text
    txt.mark_set(INSERT, END)
    #  get starting text position
    st = txt.index('insert')
    #  Add text to text widget at the end
    txt.insert(END, tstr)
    #  get ending text position
    ed = txt.index('insert')
    # print "Start = {}  End = {}  String = {}".format(st,ed,str)   #  debug
    #  tag area bound by start and stop
    txt.tag_add("junk6", st, ed)
    #  Change color of tagged area
    txt.tag_config("junk6", foreground='lightgrey')
    #  Go to end of text window (auto scroll)
    txt.see(END)
    #  Update idle tasks
    txt.update_idletasks()
    # disable changes to text widget
    txt.configure(state='disabled')


def to_log_violet(txt, tstr):
    """Sends string to text window in violet """
    # Enable changes to text widget
    txt.configure(state='normal')
    # position cursor at the end of the text
    txt.mark_set(INSERT, END)
    #  get starting text position
    st = txt.index('insert')
    #  Add text to text widget at the end
    txt.insert(END, tstr)
    #  get ending text position
    ed = txt.index('insert')
    # print "Start = {}  End = {}  String = {}".format(st,ed,str)   #  debug
    #  tag area bound by start and stop
    txt.tag_add("junk7", st, ed)
    #  Change color of tagged area
    txt.tag_config("junk7", foreground='violet')
    #  Go to end of text window (auto scroll)
    txt.see(END)
    #  Update idle tasks
    txt.update_idletasks()
    # disable changes to text widget
    txt.configure(state='disabled')


def clear_log(txt):
    """Clear the text widget. """
    #  Enable writing to text widget
    txt.configure(state='normal')
    #  Delete from first position to end
    txt.delete(1.0, END)
    #  Disable writing to text widget
    txt.configure(state='disabled')


def save_log(txt, main):
    """Get all text from existing text widget and save it to a 
    user defined text file. """
    lines = txt.get("1.0", END).splitlines()
    path = filedialog.asksaveasfilename(parent=main)
    if path == '':
        return
    fo = open(path, 'w', encoding='utf-8')
    for line in lines:
        fo.write(line + "\n")
    fo.close()


if __name__ == "__main__":
    from tkinter import *
    from tkinter import ttk


    def quit_prog():
        root.destroy()


    def my_clear_log():
        clear_log(txt)


    def my_save_log():
        save_log(txt, mainframe)


    def test_log():
        to_log(txt, 'Name:\n' + get_full_lib_version() + '\n')
        to_log(txt, 'Sample Text Normal\n')
        to_log_blue(txt, 'Sample Text Blue\n')
        to_log_cyan(txt, 'Sample Text Cyan\n')
        to_log_red(txt, 'Sample Text Red\n')
        to_log_violet(txt, 'Sample Text Violet\n')
        to_log_yellow(txt, 'Sample Text Yellow\n')
        to_log_green(txt, 'Sample Text Green\n')
        to_log_white(txt, 'Sample Text White\n')


    root = Tk()
    #  prevent window resizing.
    root.resizable(0, 0)
    # Replace tk icon with your own.
    root.title('Testing Log file')

    mainframe = ttk.Frame(root, padding="3", height=680, width=650)
    mainframe.grid(column=1, row=2, sticky=(N, W, E, S))
    mainframe.grid_propagate(0)

    clearlog = ttk.Button(mainframe, text="Clear Log", style='cyan.TButton', command=my_clear_log, width=15)
    clearlog.grid(column=0, row=1, padx=15, pady=5)
    savelog = ttk.Button(mainframe, text="Save Log", style='cyan.TButton', command=my_save_log, width=15)
    savelog.grid(column=1, row=1, padx=15, pady=5)
    testProg = ttk.Button(mainframe, text="TEST", style='red.TButton', command=test_log, width=15)
    testProg.grid(column=0, row=2, padx=15, pady=5)
    quitProg = ttk.Button(mainframe, text="Quit", style='red.TButton', command=quit_prog, width=15)
    quitProg.grid(column=1, row=2, padx=15, pady=5)
    s = 'Filename : ' + get_full_lib_version() + ']\n'
    lab2 = Label(mainframe,text=s)
    lab2.grid(column=2,row=0, columnspan=6)

    #  Text box Widget
    txt = Text(mainframe, width=45, height=34, fg='lightgreen', bg='black', padx=15, pady=15)
    txt.grid(column=2, row=1, columnspan=6, rowspan=20, sticky="nsew")
    txt.insert(1.0, "Start log file\n")
    txt.configure(state='disabled')

    #  Scrollbar linked to text box above
    scrollb = ttk.Scrollbar(mainframe, command=txt.yview)
    scrollb.grid(row=1, column=7, rowspan=20, sticky='nse')
    txt['yscrollcommand'] = scrollb.set

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()
