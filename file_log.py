# pylint: disable=unused-wildcard-import, method-hidden
# 
# #---------------------------------------------------------------------------
# Name:        file_log
# Purpose:
#
# Author:      PHedlund
#
# Created:     02/06/2021
# Copyright:   (c) PHedlund 2021
#---------------------------------------------------------------------------
"""    Logging Function Library
    get_lib_version
    get_full_lib_version
    file_log
    log
    log_dt
    header   
"""
##  ------------------------------------------------------------------------
##  Imports
##  ------------------------------------------------------------------------
import os, sys
import time
from datetime import datetime

##  ------------------------------------------------------------------------
##  Classes
##  ------------------------------------------------------------------------


class file_log():
    """
        Logging functions
        Logging data to a file

        get_lib_version() Returns version of code

        get_full_lib_version() Returns class name, version and date

        log()  Sends a string out to log file
        log_dt() Sends the date / time and string out to the log file
        header() Sends a header (depending on type and dt_type) out to 
            the log file       
        ##  INTERNAL FUNCTIONS  ##
        ch_line() Creates len amount of the character ch

        gen_fix_str() Generates a fixed string padded with spaces on the left
        SAMPLE USEAGE

        log1 = file_log(my_fn, fpath = my_path, new_f = 1)

        log1.header(1, 'Writing to new log file 1') # NO CR
        log1.log('Sample data to new log\n')        # CR added
        log1.log_dt('Sample data with date/time\n') # CR added """

    name_file_log    = 'file_log.py'
    version_file_log = '1.1.0'
    date_file_log    = '04/30/21'
    author_file_log  = 'Peter A. Hedlund'

    LIB_NAME = name_file_log
    LIB_VERSION = version_file_log
    LIB_DATE = date_file_log
    LIB_AUTHOR = author_file_log


    def __init__(self, fname, fpath = os.path.dirname(sys.argv[0]), new_f = 1):    
        self.fname = fname
        self.fpath = fpath
        self.new_f = new_f
        self.full_file = self.fpath + '/' + self.fname
        if self.new_f == 1:
            fp = open(self.full_file, 'w', encoding='utf-8')
            fp.close()


    # Public Function
    def get_lib_version(self): 
        """    Returns version information only. """
        return self.LIB_VERSION 


    # Public Function
    def get_full_lib_version(self):
        """Returns version information and library name.""" 
        msg = self.get_lib_version()
        rs = 'Library Name : ' + self.LIB_NAME + '\nVersion : ' + msg
        rs = rs + '\nDate : ' + self.LIB_DATE
        rs = rs + '\nAuthor : ' + self.LIB_AUTHOR + '\n'
        return rs


    def log(self, wstr):
        """ Opens file in append, writes string to file then closes the
        file.  User is responsible for carrage return character \\n """
        fp = open(self.full_file, 'a', encoding='utf-8')
        fp.write(wstr)
        fp.close()


    def log_dt(self, wstr):
        """ Open file in append, writes date / time to the file then the
        passed string wstr. closing the file when done. The user is 
        responsible for added a carrage return character \\n """
        now = datetime.now()
        dt = now.strftime('%m/%d/20%y %H:%M:%S ')
        self.log(dt + wstr)


    def ch_line(self, ch, ln):
        """ This routine creates a string of character ch at a given
        length (for header function) """
        ostr = ''
        x = 0
        while x < ln:
            ostr = ostr + ch
            x = x + 1
        return ostr


    def gen_fix_str(self, wstr, ln):
        ad = self.ch_line(' ', ln - len(wstr))
        return wstr + ad


    def header(self, type, dt_type, wstr):
        """ This routine creates a header log entry depending on type,
        0 Simple -= string =-
        1 Double Line box 
        2 Single line Box 
        3 C Style header
        4 Python Style Header 
        dt_type
        0 NONE
        1 Date
        2 Time
        3 Date and time
        This routine provies the needed carrage returns."""
        now = datetime.now()
        mx_len = len(wstr)
        if mx_len < 10:
            mx_len = 10
        s1 = self.gen_fix_str(wstr, mx_len)
        if (dt_type & 1) == 1 :
            ts = now.strftime('%H:%M:%S')
            s2 = self.gen_fix_str( ts, mx_len)   
        if (dt_type & 2) ==  2:
            ds = now.strftime('%m/%d/20%y')
            s3 = self.gen_fix_str(ds, mx_len)   

        if type == 1:  #  Double Line Box
            bl = self.ch_line('=', mx_len + 4)
            self.log(bl + '\n')
            self.log('| ' + s1 + ' |\n')
            if (dt_type & 1) == 1:
                self.log('| ' + s2 + ' |\n' )
            if (dt_type & 2) == 2:    
                self.log('| ' + s3 + ' |\n' )
            self.log(bl + '\n')
        elif type == 2:  #  Single Line Box
            bl = self.ch_line('-', len(wstr) + 2)
            self.log('+' + bl + '+\n')
            self.log('| ' + wstr + ' |\n')
            if (dt_type & 1) == 1:
                self.log('| ' + s2 + ' |\n' )
            if (dt_type & 2) == 2:    
                self.log('| ' + s3 + ' |\n' )
            self.log('+' + bl + '+\n')
        elif type == 3:  #  C style Header
            bl = self.ch_line('-', len(wstr) + 2)
            self.log('// ' + bl + '\n')
            self.log('//  ' + wstr + '\n')
            if (dt_type & 1) == 1:
                self.log('// ' + s2 + '\n' )
            if (dt_type & 2) == 2:    
                self.log('// ' + s3 + '\n' )
            self.log('// ' + bl + '\n')
        elif type == 4:  #  Python Style Header
            bl = self.ch_line('-', len(wstr) + 2)
            self.log('# ' + bl + '\n')
            self.log('#  ' + wstr + '\n')
            if (dt_type & 1) == 1:
                self.log('# ' + s2 + '\n' )
            if (dt_type & 2) == 2:    
                self.log('# ' + s3 + '\n' )
            self.log('# ' + bl + '\n')
        else:  #  Default Header Style (Sweet and simple)
            self.log('-= ' + wstr + ' =-\n')
            if (dt_type & 1) == 1:
                self.log('-= ' + s2 + ' =-\n' )
            if (dt_type & 2) == 2:    
                self.log('-= ' + s3 + ' =-\n' )


if __name__ == "__main__":

    from tkinter import *
    import tkinter as tk
    import mylib.scrn_log

##  ------------------------------------------------------------------------
##  Controls
##  ------------------------------------------------------------------------

    def quit_prog():
        global root
        root.destroy()

    def btn_create():
        log1.header(0, 0, 'Log to new log file 1 Header 0 ,0')
        log1.header(1, 0, 'Log to new log file 1 Header 1, 0')
        log1.header(2, 0, 'Log to new log file 1 Header 2, 0')
        log1.header(3, 0, 'Log to new log file 1 Header 3, 0')
        log1.header(4, 0, 'Log to new log file 1 Header 4, 0')
        log1.header(1, 0, 'Header Big type 1, 0')
        log1.header(1, 1, 'Header Big type 1, 1')
        log1.header(1, 2, 'Header Big type 1, 2')
        log1.header(1, 3, 'Header Big type 1, 3')
        log1.header(2, 0, 'Header Big type 2, 0')
        log1.header(2, 1, 'Header Big type 2, 1')
        log1.header(2, 2, 'Header Big type 2, 2')
        log1.header(2, 3, 'Header Big type 2, 3')
        log1.log('Sample data to new log\n')
        log1.log_dt('Date/Time Sample\n')
        mylog.log_scrn('Created log file\n')
        

    def btn_append():
        log2.header(0, 0, 'Log to existing log file 2 Header 0, 0')
        log2.header(0, 1, 'Log to existing log file 2 Header 0, 1')
        log2.header(0, 2, 'Log to existing log file 2 Header 0, 2')
        log2.header(0, 3, 'Log to existing log file 2 Header 0, 3')
        log2.header(2, 0, 'Log to existing log file 2 Header 2, 0')
        log2.log('Sample data to existing log\n')
        log2.log_dt('Date/Time Sample\n')
        mylog.log_scrn('appended log file\n')

    def btn_clear():
        mylog.clear_scrn()

    def btn_view():
        fp = open(mfn, 'r')
        while True:
            line = fp.readline()
            if not line:
                break
            mylog.log_scrn(line)
        fp.close()


    my_fn = 'test.log'
    my_path = 'n:/store/python/converted/scrap'
    mfn = my_path + '/' + my_fn
    root = tk.Tk()
    root.geometry("1400x650")
    root.geometry('%dx%d+%d+%d' % (520, 600, 20,   20))

    root.title("Logging Demonstration")

    log1 = file_log(my_fn, fpath = my_path, new_f = 1)
    log2 = file_log(my_fn, fpath = my_path, new_f = 0)
    brow = 0
    btn1 = tk.Button(root, text='Create Log File', command=btn_create)
    btn1.grid(column=0, row=brow)
    brow += 1
    btn2 = tk.Button(root, text='Append Log File', command=btn_append)
    btn2.grid(column=0, row=brow)
    brow += 1
    btn3 = tk.Button(root, text='View Log file', command=btn_view)
    btn3.grid(column=0, row=brow)
    brow += 1
    btn4 = tk.Button(root, text='Clear Window', command=btn_clear)
    btn4.grid(column=0, row=brow)
    brow += 1
    
    btn5 = tk.Button(root, text='Quit', command=quit_prog)
    btn5.grid(column=0, row=brow)
    # Text box Widget
    mylog = mylib.scrn_log.scrn_log(root, 45, 34, 'lightgreen', 'black', 2, 0, 6, 20)


    for child in root.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()

