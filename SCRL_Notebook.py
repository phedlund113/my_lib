# -*- coding: utf-8 -*-

# Copyright (c) Muhammet Emin TURGUT 2020
# For license see LICENSE
# https://github.com/muhammeteminturgut/ttkScrollableNotebook
#
# Modifications by Peter Hedlund


from tkinter import *
from tkinter import ttk
name_SCRL_Notebook    = 'SCRL_Notebook.py'
version_SCRL_Notebook = '1.0.0'
date_SCRL_Notebook    = '04/26/21'
author_SCRL_Notebook  = 'Muhammet Emin TURGUT'
LIB_NAME = name_SCRL_Notebook
LIB_VERSION = version_SCRL_Notebook
LIB_DATE = date_SCRL_Notebook
LIB_AUTHOR = author_SCRL_Notebook


class ScrollableNotebook(ttk.Frame):
    """Scrollable Notebook widget (Similar to ttk.Notebook)"""
    
    def __init__(self,parent,wheelscroll=False,tabmenu=False,*args,**kwargs):
        ttk.Frame.__init__(self, parent, *args)
        self.xLocation = 0
        self.notebookContent = ttk.Notebook(self,**kwargs)
        self.notebookContent.pack(fill="both", expand=True)
        self.notebookTab = ttk.Notebook(self,**kwargs)
        self.notebookTab.bind("<<NotebookTabChanged>>",self._tabChanger)
        if wheelscroll==True: self.notebookTab.bind("<MouseWheel>", self._wheelscroll)
        slideFrame = ttk.Frame(self)
        slideFrame.place(relx=1.0, x=0, y=1, anchor=NE)
        self.menuSpace=30
        if tabmenu==True:
            self.menuSpace=50
            bottomTab = ttk.Label(slideFrame, text=" \u2630 ")
            bottomTab.bind("<1>",self._bottomMenu)
            bottomTab.pack(side=RIGHT)
        leftArrow = ttk.Label(slideFrame, text=" \u276E")
        leftArrow.bind("<1>",self._leftSlide)
        leftArrow.pack(side=LEFT)
        rightArrow = ttk.Label(slideFrame, text=" \u276F")
        rightArrow.bind("<1>",self._rightSlide)
        rightArrow.pack(side=RIGHT)
        self.notebookContent.bind("<Configure>", self._resetSlide)

    def get_lib_version(self):
        """Returns version information only."""
        return LIB_VERSION


    def get_full_lib_version(self):
        """Returns version information and library name."""
        msg = self.get_lib_version()
        rs = 'Library Name : ' + LIB_NAME + '\nVersion : ' + msg
        rs = rs + '\nDate : ' + LIB_DATE
        rs = rs + '\nAuthor : ' + LIB_AUTHOR + '\n' 
        return rs

    def _wheelscroll(self, event):
        if event.delta > 0:
            self._leftSlide(event)
        else:
            self._rightSlide(event)

    def _bottomMenu(self,event):
        tabListMenu = Menu(self, tearoff = 0)
        for tab in self.notebookTab.tabs():
            tabListMenu.add_command(label=self.notebookTab.tab(tab, option="text"),command= lambda temp=tab: self.select(temp))
        try: 
            tabListMenu.tk_popup(event.x_root, event.y_root) 
        finally: 
            tabListMenu.grab_release()

    def _tabChanger(self,event):
        try: self.notebookContent.select(self.notebookTab.index("current"))
        except: pass

    def _rightSlide(self,event):
        if self.notebookTab.winfo_width()>self.notebookContent.winfo_width()-self.menuSpace:
            if (self.notebookContent.winfo_width()-(self.notebookTab.winfo_width()+self.notebookTab.winfo_x()))<=self.menuSpace+5:
                self.xLocation-=20
                self.notebookTab.place(x=self.xLocation,y=0)
    def _leftSlide(self,event):
        if not self.notebookTab.winfo_x()== 0:
            self.xLocation+=20
            self.notebookTab.place(x=self.xLocation,y=0)

    def _resetSlide(self,event=None):
        self.notebookTab.place(x=0,y=0)
        self.xLocation = 0

    def add(self,frame,**kwargs):
        if len(self.notebookTab.winfo_children())!=0:
            self.notebookContent.add(frame, text="",state="hidden")
        else:
            self.notebookContent.add(frame, text="")
        self.notebookTab.add(ttk.Frame(self.notebookTab),**kwargs)

    def forget(self,tab_id):
        self.notebookContent.forget(self.__ContentTabID(tab_id))
        self.notebookTab.forget(tab_id)

    def hide(self,tab_id):
        self.notebookContent.hide(self.__ContentTabID(tab_id))
        self.notebookTab.hide(tab_id)

    def identify(self,x, y):
        return self.notebookTab.identify(x,y)

    def index(self,tab_id):
        return self.notebookTab.index(tab_id)

    def __ContentTabID(self,tab_id):
        return self.notebookContent.tabs()[self.notebookTab.tabs().index(tab_id)]

    def insert(self,pos,frame, **kwargs):
        self.notebookContent.insert(pos,frame, **kwargs)
        self.notebookTab.insert(pos,frame,**kwargs)

    def select(self,tab_id=None):
        if tab_id == None:
            return self.notebookTab.select()
##        self.notebookContent.select(self.__ContentTabID(tab_id))
        self.notebookTab.select(tab_id)
    
    def tab(self,tab_id, option=None, **kwargs):
        kwargs_Content = kwargs.copy()
        kwargs_Content["text"] = "" # important
        self.notebookContent.tab(self.__ContentTabID(tab_id), option=None, **kwargs_Content)
        return self.notebookTab.tab(tab_id, option=None, **kwargs)

    def tabs(self):
##        return self.notebookContent.tabs()
        return self.notebookTab.tabs()

    def enable_traversal(self):
        self.notebookContent.enable_traversal()
        self.notebookTab.enable_traversal()

if __name__ == "__main__":

    root=Tk()
    root.title("Example")
    notebook=ScrollableNotebook(root,wheelscroll=True,tabmenu=True)
    frame1=Frame(notebook)
    frame2=Frame(notebook)
    frame3=Frame(notebook)
    frame4=Frame(notebook)
    notebook.add(frame1,text="I am Tab One")
    notebook.add(frame2,text="I am Tab Two")
    notebook.add(frame3,text="I am Tab Three")
    notebook.add(frame4,text="I Forgot How to Count")
    notebook.pack(fill="both",expand=True)
    text=Text(frame1)
    text.pack()
    Label(frame2,text="I am Frame 2").pack()
    Label(frame3,text="I am Frame 3").pack()
    Label(frame4,text="You know i'm Frame 4").pack()
    text.insert(INSERT,"Hello World!")
    root.mainloop()        