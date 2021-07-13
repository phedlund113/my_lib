# pylint: disable=unused-wildcard-import, method-hidden
# 
# #---------------------------------------------------------------------------
# Name:        gage
# Purpose:
#
# Author:      PHedlund
#
# Created:     01/06/2021
# Copyright:   (c) PHedlund 2021
#---------------------------------------------------------------------------
""" Gage Function Library
    get_lib_version
    get_full_lib_version
    gage
    gage.draw_value
"""
##  ------------------------------------------------------------------------
##  Imports
##  ------------------------------------------------------------------------
import math
from tkinter import *
import tkinter as tk


##  ------------------------------------------------------------------------
##  Classes
##  ------------------------------------------------------------------------


class gage(object):
    """ Graphic Guage, this will sit on a existing canvas cnvs
        orgx and orgy are the starting points
        widx, and widy are the width
        color is the color of the guage
        angst is the starting angle (0 is at the bottom center)
        angln is the number of degrees the guage is drawn to

        get_lib_version() Returns version of code

        get_full_lib_version() Returns class name, version and date

        draw_value() will calculate the angle based on set_range()
            then call draw_angle() to draw the pointer.

        ##  INTERNAL FUNCTIONS  ##

        get_x_y() given the angle and diameter returns the x, y point
        from center to draw a line.

        draw_ticks() will place ticks from outside arc to inside arc
        equidistant based on count

        draw_angle(angle,color) draws line from center to outside arc
            angle 0 is pointed straight down, using color provided

        clear_line()  erases the last line drawn with draw_angle()

        set_range() will calculate the angles per count given max and min
        values.

        set_label() will place a text label at the bottom center of the gage
        
        To Simplify the creation and management of the gauges, i have decided
        to use a dictionary to set all inital values to the gauge 

        SAMPLE USEAGE
        # assume cv is the canvas object and you are displaying 
          an altitude gauge

        alt_mtr = {'X1': 50, 'Y1': 50, 'X2':150, 'Y2':150, 
           'color': 'black', 'angl_st': 40 , 'angl_ln' : 280, 
           'rng_lo':0, 'rng_hi': 1000,
           'title': 'Altitude', 'num_ticks': 10}

        g = guage(cv, alt_mtr)
        g.draw_value(100, 'red')  """

    name_gage    = 'gage.py'
    version_gage = '1.0.0'
    date_gage    = '07/15/20'
    author_gage  = 'Peter A. Hedlund'
    
    LIB_NAME = name_gage
    LIB_VERSION = version_gage
    LIB_DATE = date_gage
    LIB_AUTHOR = author_gage
    
    # LIB_NAME = 'gage.py'
    # LIB_VERSION = '1.0.0'
    # LIB_DATE = '7/15/20'
    line_id = None
    deg_point = 0.0
    min_r = 0
    max_r = 0
    ctrx = 0
    ctry = 0
    text_id = None


    def __init__(self, cnvs, mtr_info):
    #  orgx1, orgy1, orgx2, orgy2, color, angst, angln):
        self.cnvs = cnvs
        self.orgx1 = mtr_info['X1']
        self.orgy1 = mtr_info['Y1']
        self.orgx2 = mtr_info['X2']
        self.orgy2 = mtr_info['Y2']
        self.color = mtr_info['color']
        self.angst = mtr_info['angl_st']
        self.angln = mtr_info['angl_ln']
        self.rng_st = mtr_info['rng_lo']
        self.rng_len = mtr_info['rng_hi']
        self.title = mtr_info['title']
        self.ticks = mtr_info['num_ticks']

        self.dia = (self.orgx2 - self.orgx1)/2
        self.ctrx = ((self.orgx2-self.orgx1)/2)+self.orgx1
        self.ctry = ((self.orgy2-self.orgy1)/2)+self.orgy1
        self.cnvs.create_arc(self.orgx1, self.orgy1,
            self.orgx2, self.orgy2,
            start=270 + self.angst, extent=self.angln,
            width=3, style =ARC)
        self.cnvs.create_arc(self.orgx1+10, self.orgy1+10,
            self.orgx2-10, self.orgy2-10,
            start=270 + self.angst, extent=self.angln,
            width=3, style =ARC)
        self.cnvs.create_rectangle(self.orgx1 - 30, self.orgy1 - 25,
                                   self.orgx2 + 30, self.orgy2 + 20, width=3)
        self.set_range(self.rng_st,self.rng_len)
        self.set_label(self.title)
        self.draw_ticks(self.ticks)


    # Public Function
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


    def get_x_y(self, angle, radius):
        if angle > 360:
            angle %= 360
        q = int(angle / 90)
        angle = angle % 90

        dia = self.ctrx - self.orgx1
        # dia2 = self.ctry - self.orgy1
        dia = radius

        x = dia * math.cos(math.radians(angle))
        y = dia * math.sin(math.radians(angle))
        point2 = [[self.ctrx-y, self.ctry+x],[self.ctrx-x, self.ctry-y],
                  [self.ctrx+y, self.ctry-x],[self.ctrx+x, self.ctry+y]]
        return point2[q][0], point2[q][1]


    def draw_ticks(self, count):
        a_count = self.angln / count
        a_org = (360 - self.angln) / 2
        incr = (self.max_r - self.min_r) / count

        for x in range(0, count+1):
            angl = a_org + (x * a_count)
            x1,y1 = self.get_x_y(angl, self.dia)
            x2,y2 = self.get_x_y(angl, self.dia - 10)
            self.cnvs.create_line(x1, y1, x2, y2, width=2)
            x1,y1 = self.get_x_y(angl, self.dia+15)
            lbl = int(self.min_r + (incr * x))
            self.cnvs.create_text(x1, y1, text=str(lbl))


    def draw_angle(self, anl, color):
        x2, y2 = self.get_x_y(anl, self.dia)
        self.line_id = self.cnvs.create_line(self.ctrx, self.ctry,x2, y2,
            width=2, fill=color, arrow=LAST)


    def clear_line(self):
        self.cnvs.delete(self.line_id)


    def set_range(self, min_rng, max_rng):
        self.min_r = min_rng
        self.max_r = max_rng
        self.deg_point = (max_rng - min_rng) / self.angln


    def set_label(self, text2):
        self.cnvs.create_text(self.ctrx,self.orgy2,text=text2)

    # Public Function
    def draw_value(self, value, color):
        """draw_value() will calculate the angle based on set_range()
        then call draw_angle() to draw the pointer. with selected color."""

        if self.deg_point == 0.0:
            return
        v = (value - self.min_r) / self.deg_point
        self.clear_line()
        st = (360 - self.angln) / 2
        self.draw_angle(v + st, color)
        self.cnvs.delete(self.text_id)
        self.text_id = self.cnvs.create_text(self.ctrx, self.orgy2-15,
            text=str(value))



if __name__ == "__main__":
    from tkinter import *
    from tkinter import ttk

##  ------------------------------------------------------------------------
##  Controls
##  ------------------------------------------------------------------------

    def quit_prog():
        global root
        root.destroy()


    def upd_fuel(_f_):
        fuel.draw_value(int(_f_), 'red')


    def upd_speed(_s_):
        speed.draw_value(int(_s_), 'red')


    root = tk.Tk()
    root.geometry("1400x650")
    root.geometry('%dx%d+%d+%d' % (380, 250, 20,   20))

    root.title("Gage Demonstration")

    cv = tk.Canvas(root, height="180", width=380, bg='white')

    cv.grid(column=0, row=1, columnspan=10)

    speed_mtr = {'X1': 50, 'Y1': 50, 'X2':150, 'Y2':150, 
                'color': 'black', 'angl_st': 40 , 'angl_ln' : 280, 
                'rng_lo':-100, 'rng_hi': 100,
                'title': 'Speed', 'num_ticks': 10}
    speed = gage(cv, speed_mtr)
    speed.draw_value(0, 'red')

    fuel_mtr = {'X1': 230, 'Y1': 50, 'X2':330, 'Y2':150, 
                'color': 'black', 'angl_st': 40 , 'angl_ln' : 280, 
                'rng_lo':0, 'rng_hi': 2000,
                'title': 'Fuel', 'num_ticks': 10}
    fuel = gage(cv, fuel_mtr)
    fuel.draw_value(0, 'red')

    pdx = 5
    sl1 = tk.Scale(root, label='Speed',from_=-100, to=100,orient=tk.HORIZONTAL,
                command=upd_speed)
    sl1.grid(column=0, row=2, padx=pdx)
    sl1 = tk.Scale(root, label='Fuel',from_=0, to=2000,orient=tk.HORIZONTAL,
                command=upd_fuel)
    sl1.grid(column=1, row=2, padx=pdx)
    sdirh = tk.Button(root, text='  Quit  ', command=quit_prog, bg='saddlebrown',
        fg='yellow')
    sdirh.grid(column=2, row=2, padx=pdx)

    root.mainloop()

