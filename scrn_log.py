#
# pylint: disable=unused-wildcard-import, method-hidden
#
""" Logging functions Library
    scrn_log() 
    get_lib_version() Show numeric version of library.
    get_lib_full_version()  Show numeric version and library filename.
    log_scrn()  sends string to text window in last color
    log_scrn_color()  sends string to text window in color
        Acceptable colors are 'red','yellow','green','blue''cyan'
        'white', 'violet', sky blue, hot pink, lightgrey, and brown4
    clear_scrn()  clears the text window
    save_scrn()  saves the text window to a user selected file
"""

from tkinter import *
from tkinter import filedialog
from tkinter import ttk

name_scrn_log    = 'scrn_log.py'
version_scrn_log = '1.1.0'
date_scrn_log    = '04/29/21'
author_scrn_log  = 'Peter A. Hedlund'

LIB_NAME = name_scrn_log
LIB_VERSION = version_scrn_log
LIB_DATE = date_scrn_log
LIB_AUTHOR = author_scrn_log

class scrn_log(object):
    """frame=mainframe, wd=width, ht=height, fgc=foreground color,
    bgc=background color, col=column, rw=row, cs=columnspan, rs=rowspan"""
    
    update = 1   #  Set to 0 to speed up screen writes in loops

    def __init__(self, frame, wd, ht, fgc, bgc, col, rw, cs, rs ):
    #  Text box Widget
        txt = Text(frame, width=wd, height=ht, fg=fgc, bg=bgc, padx=2, pady=2)
        txt.grid(column=col, row=rw, columnspan=cs, rowspan=rs, sticky="nsew",
        padx=5, pady=5)
        txt.configure(state='disabled')
        #  Scrollbar linked to text box above
        scrollb = ttk.Scrollbar(frame, command=txt.yview)
        scrollb.grid(column=col+cs+1, row=rw, rowspan=rs, sticky='nse')
        txt['yscrollcommand'] = scrollb.set
        self.txt = txt
        self.colors = {'red': 'junk1','yellow': 'junk2','green': 'junk3',
        'blue': 'junk4','cyan': 'junk5','white': 'junk6','violet':'junk7',
        'sky blue': 'junk8', 'hot pink': 'junk9', 'lightgrey':'junk10', 
        'brown4':'junk11'}

    def get_lib_version(self):
        """Returns version information only."""
        return LIB_VERSION


    def get_full_lib_version(self):
        """Returns version information and library name."""
        msg = self.get_lib_version()
        rs = 'Library Name : ' + LIB_NAME + '\nVersion : ' + msg
        rs = rs + "\nDate : " + LIB_DATE
        rs = rs + '\nAuthor : ' + LIB_AUTHOR + '\n'
        return rs


    def log_scrn(self, tstr):
        """Sends string to text window. """
        self.txt.configure(state='normal')
        self.txt.index(END)
        self.txt.see(END)
        self.txt.insert(END, tstr)
        if self.update == 1:
            self.txt.update()
        self.txt.configure(state='disabled')


    def log_scrn_color(self, tstr, color):
        """ Sends the string to the text window in specified color
        see colors dictionary in the init section for color selection
        Current Colors : 'red','yellow','green','blue','cyan','white',
        'violet', 'sky blue', 'hot pink', 'lightgrey', and 'brown4'"""
        if (color in self.colors) == False:
            color = 'green'
        self.txt.configure(state='normal')
        self.txt.mark_set(INSERT, END)
        st = self.txt.index('insert')
        self.txt.insert(END, tstr)
        ed = self.txt.index('insert')
        self.txt.tag_add(self.colors[color], st, ed)
        self.txt.tag_config(self.colors[color], foreground=color)
        self.txt.see(END)
        if self.update == 1:
            self.txt.update_idletasks()
        self.txt.configure(state='disabled')

    
    def log_scrn_raw(self, tstr):
        """Sends string to text window. low overhead for multiple calls. """
        self.txt.configure(state='normal')
        self.txt.insert(END, tstr)
        self.txt.configure(state='disabled')


    def get_pos(self):
        """ returns current position of cursor x.y """
        self.txt.configure(state='normal')
        rval = self.txt.index(INSERT)
        self.txt.configure(state='disabled')
        return  rval


    def clear_scrn(self):
        """Clear the text widget. """
        #  Enable writing to text widget
        self.txt.configure(state='normal')
        #  Delete from first position to end
        self.txt.delete(1.0, END)
        #  Disable writing to text widget
        self.txt.configure(state='disabled')


    def save_scrn(self, main):
        """Get all text from existing text widget and save it to a
        user defined text file. NO COLORED TEXT"""
        lines = self.txt.get("1.0", END).splitlines()
        path = filedialog.asksaveasfilename(parent=main)
        if path == '':
            return
        fo = open(path, 'w', encoding='utf-8')
        for line in lines:
            fo.write(line + "\n")
        fo.close()


    def clipboard_scrn(self, main):
        """Get all text from existing text widget and save it to 
        the clipboard"""
        lines = self.txt.get("1.0", END).splitlines()
        main.clipboard_clear()
        for line in lines:
            main.clipboard_append(line + '\n')
        main.update() 


if __name__ == "__main__":
    from tkinter import *
    from tkinter import ttk
    import os
    import sys

    def quit_prog():
        root.destroy()


    def my_clear_log():
        screen.clear_scrn()


    def log_clip():
        screen.clipboard_scrn(mainframe)


    def my_save_log():
        screen.save_scrn(mainframe)


    def get_position():
        pos = screen.get_pos()
        screen.log_scrn(f'Position is {pos}\n')
        

    def part_text():
        screen.log_scrn('no CR on this line ')

        
    def test_log():
        screen.log_scrn('Name ' + os.path.basename(sys.argv[0]) + '\n' + screen.get_full_lib_version() + '\n')
        screen.log_scrn('Sample Text Normal\n')
        screen.log_scrn_color('Sample Text Blue\n', 'blue')
        screen.log_scrn_color('Sample Text Cyan\n', 'cyan')
        screen.log_scrn_color('Sample Text Red\n','red')
        screen.log_scrn_color('Sample Text Violet\n','violet')
        screen.log_scrn_color('Sample Text Yellow\n', 'yellow')
        screen.log_scrn_color('Sample Text Green\n', 'green')
        screen.log_scrn_color('Sample Text White\n', 'white')
        screen.log_scrn_color('Sample Text Sky Blue\n', 'sky blue')
        screen.log_scrn_color('Sample Text Hot Pink\n', 'hot pink')
        screen.log_scrn_color('Sample Text Light Grey\n', 'lightgrey')
        screen.log_scrn_color('Sample Text Brown\n', 'brown4')
        screen.log_scrn('to_log function without color\n')

    root = Tk()
    #  prevent window resizing.
    root.resizable(0, 0)
    # Replace tk icon with your own.
    root.title('Testing Log file')

    mainframe = ttk.Frame(root, padding="3", height=650, width=700)
    mainframe.grid(column=1, row=2, sticky=(N, W, E, S))
    mainframe.grid_propagate(0)

    s1 = ttk.Style()
    s1.configure('red.TButton', background='Red', relief='sunken')
    s2 = ttk.Style()
    s2.configure('blue.TButton', background='Blue')
    s3 = ttk.Style()
    s3.configure('green.TButton', background='Green')
    s4 = ttk.Style()
    s4.configure('cyan.TButton', background='Cyan', relief='raised')

    btn = (('Clear Log', my_clear_log, 'cyan.TButton'),
           ('Save Log', my_save_log, 'cyan.TButton'),
           ('TEST', test_log, 'red.TButton'),
           ('Text no LF', part_text, ''),
           ('Get Pos', get_position, ''),
           ('Log 2 Clipboard', log_clip, 'blue.TButton' ),
           ('Quit', quit_prog, 'red.TButton'))

    for x in range(0, len(btn)):
        bbtn = ttk.Button(mainframe, text=btn[x][0], command=btn[x][1], 
                style=btn[x][2], width=15) 
        bbtn.grid(column=0, row=x+1, padx=15, pady=5)          
    
    screen = scrn_log(mainframe, 50, 34, 'lightgreen', 'black', 2, 1, 6, 20)
    s = 'Filename : Version [' + screen.get_full_lib_version() + ']\n'
    lab2 = Label(mainframe,text=s)
    lab2.grid(column=2,row=0, columnspan=2)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()
