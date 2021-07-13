#
# pylint: disable=unused-wildcard-import, method-hidden
# 

# #---------------------------------------------------------------------------
# Name:        clock_face
# Purpose:
#
# Author:      PHedlund
#
# Created:     09/09/2020
# Copyright:   (c) PHedlund 2020
#---------------------------------------------------------------------------
""" See my_clock.__doc__ for details about this library. 
    get_lib_version() Show numeric version of library.
    get_lib_full_version()  Show numeric version and library filename. 
"""

import math
from tkinter import *


class my_clock(object):
    """This graphic function will display a clock on the screen. 
        Right now is has minuite hand in black and hour hand in red. 
        The red hand moves with the second hand so at 4:55 the hour
        hand is almost pointed at 4 as a mechanical clock would be. 

        get_lib_version() Returns version of code

        get_full_lib_version() Returns class name, version and date

        show_time()  Shows Hours, Mins, 

        show_full_time()  Shows Hours, Mins, Secs,

        Example Useage
        
        alt_mtr = {'X1': 30, 'Y1': 30, 'width':150 }
        pc_clock = my_clock(cv, alt_mtr)

        tm = time.localtime(time.time())
        pc_clock.show_full_time(tm.tm_hour, tm.tm_min, tm.tm_sec) """

    name_my_clock    = 'my_clock.py'
    version_my_clock = '1.0.0'
    date_my_clock    = '11/20/20'
    author_my_clock  = 'Peter A. Hedlund'
    
    LIB_NAME = name_my_clock
    LIB_VERSION = version_my_clock
    LIB_DATE = date_my_clock
    LIB_AUTHOR = author_my_clock
    
    # LIB_NAME = 'clock_face.py'
    # LIB_VERSION = '1.0.0'
    # LIB_DATE = '11/20/20'
    deg_point = 0.0
    ctrx = 0
    ctry = 0
    _hours = None
    _min = None
    _sec = None


    ##  Class Iniialization Function
    def __init__(self, cnvs, mtr_info):
    #  orgx1, orgy1, orgx2, orgy2, color, angst, angln):
        self.cnvs = cnvs
        self.orgx1 = mtr_info['X1']
        self.orgy1 = mtr_info['Y1']
        self.width = mtr_info['width']
        
        self.dia = (self.width/2)
        self.h_len = self.dia * .75
        self.m_len = self.dia * .9
        self.s_len = self.dia * .95
        self.ctrx = self.orgx1 + self.dia
        self.ctry = self.orgy1 + self.dia
        
        self.cnvs.create_oval(self.orgx1, self.orgy1,
            self.orgx1 + self.width, self.orgy1 + self.width, width=3)
        self.draw_hour_ticks(12)
        self.draw_min_ticks(60)
        self.show_time(0, 0)


    ##  Class External Function
    def get_lib_version(self): 
        """    Returns version information only. """
        return self.LIB_VERSION 


    def get_full_lib_version(self):
        """Returns version information and library name.""" 
        msg = self.get_lib_version()
        rs = 'Library Name : ' + self.LIB_NAME + '\nVersion : ' + msg
        rs = rs + '\nDate : ' + self.LIB_DATE
        rs = rs + '\nAuthor : ' + self.LIB_AUTHOR + '\n' 
        return rs


    ##  Class Internal Function
    def get_x_y(self, angle, radius):
        if angle > 360:
            angle %= 360
        q = int(angle / 90)
        angle = angle % 90
        dia = radius

        x = dia * math.cos(math.radians(angle))
        y = dia * math.sin(math.radians(angle))
        point2 = [[self.ctrx-y, self.ctry+x],[self.ctrx-x, self.ctry-y],
                  [self.ctrx+y, self.ctry-x],[self.ctrx+x, self.ctry+y]]
        return point2[q][0], point2[q][1]


    ##  Class Internal Function
    def draw_hour_ticks(self, count):
        a_count = 360  / count
        a_org = (360 ) / 2
        incr = (360 - 0) / count

        for x in range(0, count+1):
            angl = a_org + (x * a_count)
            angl %= 360
            x1,y1 = self.get_x_y(angl, self.dia)
            x2,y2 = self.get_x_y(angl, self.dia - 8)
            self.cnvs.create_line(x1, y1, x2, y2, width=2)
            x1,y1 = self.get_x_y(angl, self.dia+15)
            lbl = int(incr * x)
            if x > 0:
                self.cnvs.create_text(x1, y1, text=str(int(lbl/30)))


    ##  Class Internal Function
    def draw_min_ticks(self, count):
        a_count = 360  / count
        a_org = (360 ) / 2

        for x in range(0, count+1):
            angl = a_org + (x * a_count)
            angl %= 360
            x1,y1 = self.get_x_y(angl, self.dia)
            x2,y2 = self.get_x_y(angl, self.dia - 5)
            self.cnvs.create_line(x1, y1, x2, y2, width=2)
            x1,y1 = self.get_x_y(angl, self.dia+15)


    ##  Class Internal Function
    def draw_angle(self, anl, color, leng):
        x2, y2 = self.get_x_y(anl, self.dia * leng)
        line_id = self.cnvs.create_line(self.ctrx, self.ctry,x2, y2,
            width=2, fill=color, arrow=LAST)
        return(line_id)


    ##  Class External Function
    def show_time(self, h, m):
        """ Shows time in Hours and Mins."""
        self.cnvs.delete(self._hours)
        angl = ((h * 30) + (m / 2) + 180) % 360
        self._hours = self.draw_angle(angl, 'red', .75)
        self.cnvs.delete(self._min)
        angl = ((m * 6) + 180) % 360
        self._min = self.draw_angle(angl, 'black', .95)

    ##  Class External Function
    def show_full_time(self, h, m, s):
        """ Shows time in hours, Mins and secs."""
        self.cnvs.delete(self._hours)
        angl = ((h * 30) + (m / 2) + 180) % 360
        self._hours = self.draw_angle(angl, 'black', .60)
        self.cnvs.delete(self._min)
        angl = ((m * 6) + 180) % 360
        self._min = self.draw_angle(angl, 'black', .85)
        self.cnvs.delete(self._sec)
        angl = ((s * 6) + 180) % 360
        self._sec = self.draw_angle(angl, 'red', .95)


#
# Test Program Starts Here
#


if __name__ == "__main__":

    ##  ------------------------------------------------------------------------
    ##  Imports
    ##  ------------------------------------------------------------------------
    import os
    import sys
    import time
    import math
    from tkinter import *
    import tkinter as tk
    from tkinter import ttk
    from tkinter import font
    import winsound
    from configparser import ConfigParser


    ##  ------------------------------------------------------------------------
    ##  Classes
    ##  ------------------------------------------------------------------------


    ##  ------------------------------------------------------------------------
    ##  Controls
    ##  ------------------------------------------------------------------------


    def t_reload_time():
        tm = time.localtime(time.time())
        pc_clock.show_full_time(tm.tm_hour, tm.tm_min, tm.tm_sec)
        my_tm = f'  {tm.tm_hour:02}:{tm.tm_min:02}:{tm.tm_sec:02}'
        lbl.config(text=my_tm)
        root.after(1000, t_reload_time)


    def t_quit_prog():
        root.destroy()


    ##  ------------------------------------------------------------------------
    ##
    ##  GUI Program Starts Here
    ##
    ##  ------------------------------------------------------------------------

    root = tk.Tk()
    root.geometry("1400x650")
    root.geometry('%dx%d+%d+%d' % (210, 270, 10,   10))
    root.title("PyClock")

    cv = tk.Canvas(root, height="210", width=205, bg='white')
    cv.grid(column=0, row=1, columnspan=10)

    _font = font.Font(weight='bold')

    alt_mtr = {'X1': 30, 'Y1': 30, 'width':150 }
    pc_clock = my_clock(cv, alt_mtr)

    lbl = tk.Label(root, text='', font = _font)
    lbl.grid(column=0, row=4, columnspan=3)

    quit = tk.Button(root, text=' Quit ', command=t_quit_prog)
    quit.grid(column=2, row=5, padx=1)
    print(pc_clock.get_full_lib_version())
    t_reload_time()
    root.mainloop()

