#
# pylint: disable=unused-wildcard-import, method-hidden
# 
""" Knob.py 
This is a knob indicator widget. It can be read and written to. The knob
is user scalable as well as user colorable.
knob(cnvs, mtr_info)
get_lib_version()
get_full_lib_version()
show_angle(angl)
draw_value(val)
get_knob() returns current position
""" 

# #---------------------------------------------------------------------------
# Name:        knob
# Purpose:     Draw a knob on the canvas that will hopefully be animated
#              by the mouse. 
#
# Author:      PHedlund
#
# Created:     09/09/2020
# Copyright:   (c) PHedlund 2020
#---------------------------------------------------------------------------
""" See knob.__doc__ for details about this library. """

import math
from tkinter import *


class knob(object):
    """This graphic function will display a knob on the screen. 
        This function uses a dictionary to define knob parameters
            'X1'      Canvas X pos
            'Y1'      Canvas Y pos
            'width'   Width of knob (height and witdh the same)
            'mn_angl' Minimum Angle of adjustment
            'ticks'   Number of ticks to be shown
            'MinVal': Minimum value for knob
            'MaxVal': Maximum value for knob
            'b_color' Knobs base color
            't_color' Knobs top center color
            'p_color' knobs pointer color

        get_lib_version() Returns version of code
        get_full_lib_version() Returns class name, version and date
        show_angle() draws new line at angle and color.
        draw_value() Draws the value converted to angle.
        get_knob()   returns the value of the knob in scale."""

    name_knob    = 'knob.py'
    version_knob = '1.0.0'
    date_knob    = '01/07/21'
    author_knob  = 'Peter A. Hedlund'

    LIB_NAME = name_knob
    LIB_VERSION = version_knob
    LIB_DATE = date_knob
    LIB_AUTHOR = author_knob

    # LIB_NAME = 'knob.py'
    # LIB_VERSION = '1.0.0'
    # LIB_DATE = '01/07/21'

    value = 0
    txt_id = 0


    ##  Class Iniialization Function
    def __init__(self, cnvs, mtr_info):

        self.cnvs = cnvs
        self.orgx1 = mtr_info['X1']
        self.orgy1 = mtr_info['Y1']
        self.width = mtr_info['width']
        self.value = 0
        self.pointer = 0
        self.txt_id = 0
        self.mn_angl = mtr_info['mn_angl']
        self.ticks = mtr_info['ticks']
        self.mnval = mtr_info['MinVal']
        self.mxval = mtr_info['MaxVal']
        self.base_c = mtr_info['b_color']
        self.top_c = mtr_info['t_color']
        self.ptr_c = mtr_info['p_color']
        self.dia = (self.width/2)
        # self.h_len = self.dia * .75
        # self.m_len = self.dia * .9
        # self.s_len = self.dia * .95
        self.ctrx = self.orgx1 + self.dia + 10
        self.ctry = self.orgy1 + self.dia + 10
        # outside ring
        self.cnvs.create_oval(self.orgx1+10, self.orgy1+10,
            self.orgx1 + self.width+10, self.orgy1 + self.width+10, width=3,
            fill=self.base_c)
        # inside ring
        cng = self.width / 3
        self.cnvs.create_oval(self.orgx1 + cng+10, self.orgy1 + cng+10,
            self.orgx1 - cng+10 + self.width, self.orgy1 - cng+10 + self.width, 
            width=3, fill=self.top_c)
        self.draw_ticks(self.mn_angl,self.ticks)
        # self.value = self.show_angle(0, 'red')


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
        """ Returns the x and y points based on angle and radius."""
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
    def draw_ticks(self, start, count):
        """Draws the count number of ticks starting at angle start."""
        a_count = (360 - (start * 2))  / (count)
        a_org = start
        wval = (self.mxval - self.mnval) / count
        for x in range(0, count+1):
            angl = a_org + (x * a_count)
            angl %= 360
            x1,y1 = self.get_x_y(angl, self.dia + 2)
            x2,y2 = self.get_x_y(angl, self.dia + 8)
            self.cnvs.create_line(x1, y1, x2, y2, width=2)
            x2,y2 = self.get_x_y(angl, self.dia + 15)
            self.cnvs.create_text(x2, y2, text=str(int(wval * x)))


    ##  Class Internal Function
    def draw_angle(self, anl, leng):
        """ Draws a line at defined angle and length in  defined color."""
        x1, y1 = self.get_x_y(anl, self.dia * (leng*.43))
        x2, y2 = self.get_x_y(anl, self.dia * leng)
        line_id = self.cnvs.create_line(x1, y1,x2, y2,
            width=2, fill=self.ptr_c, arrow=LAST)
        return(line_id)


    ##  Class Exnternal Function
    def show_angle(self, angl):
        """ Delets existing line and creates a new line at angle."""
        self.cnvs.delete(self.value)
        self.value = self.draw_angle(angl, .95)


    ##  Class Internal Function
    def show_number(self, val):
        """Displays a number at the bottom center of the knob"""
        self.cnvs.delete(self.txt_id)
        x1 = self.ctrx  
        y1 = self.ctry + 12 + (self.width / 2)
        self.txt_id = self.cnvs.create_text(x1, y1, text=str(val))


    ##  Class Exnternal Function
    def draw_value(self, value):
        """ Draws the pointer with new value on the knob."""
        angle = re_scale(self.mnval, self.mxval, 360-(self.mn_angl * 2),
        value ) + self.mn_angl
        # angle = int(val) 
        self.pointer = value
        self.show_angle(angle)
        self.show_number(value)


    def get_knob(self):
        """ Returns the current value of the knob.""" 
        return self.pointer


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

    from mylib.my_math import *

    ##  ------------------------------------------------------------------------
    ##  Classes
    ##  ------------------------------------------------------------------------


    ##  ------------------------------------------------------------------------
    ##  Controls
    ##  ------------------------------------------------------------------------



    def adj_knob(val):
        volume.draw_value(int(val))
        # print(volume.get_knob())

    def t_quit_prog():
        root.destroy()


    ##  ------------------------------------------------------------------------
    ##
    ##  GUI Program Starts Here
    ##
    ##  ------------------------------------------------------------------------

    root = tk.Tk()
    root.geometry("1400x650")
    root.geometry('%dx%d+%d+%d' % (170, 240, 10,   10))
    root.title("Knob")

    cv = tk.Canvas(root, height="160", width=160, bg='white')
    cv.grid(column=0, row=1, columnspan=10)
    my_angle = IntVar()
    direct = IntVar()
    direct.set(0)
    my_angle.set(0)
    _font = font.Font(weight='bold')

    # alt_mtr = {'X1': 30, 'Y1': 30, 'width':150 }
    alt_mtr = {'X1': 20, 'Y1': 20, 'width':100 , 'mn_angl':30, 'ticks':10,
               'MinVal':0, 'MaxVal':1000, 'b_color':'azure',
               't_color': 'tomato', 'p_color':'black' }
    volume = knob(cv, alt_mtr)

    lbl = tk.Label(root, text='', font = _font)
    lbl.grid(column=0, row=4, columnspan=3)
    scl = tk.Scale(root, label='Value', from_=0, to=1000, command=adj_knob,
                    orient=tk.HORIZONTAL)
    scl.grid(column=0, row=2, padx=1)
    quit = tk.Button(root, text=' Quit ', command=t_quit_prog)
    quit.grid(column=2, row=2, padx=1)
    adj_knob(0)
    root.mainloop()

