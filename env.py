#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      USPEHED
#
# Created:     28/08/2018
# Copyright:   (c) USPEHED 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""Enviormental Varable Manipulation

get_lib_version() Show numeric version of library.
get_lib_full_version()  Show numeric version and library filename.
set_env()  Set enviromental variable
get_eng()  Get value of enviormental variable.
"""

import winreg

name_env    = 'env.py'
version_env = '2.0.0'
date_env    = '02/05/21'
author_env  = 'Peter A. Hedlund'

LIB_NAME = name_env
LIB_VERSION = version_env
LIB_DATE = date_env
LIB_AUTHOR = author_env


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


KEY_PATH = winreg.HKEY_LOCAL_MACHINE
REG_PATH = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'

def set_env(name, value):
    """Set enviromental variable. """
    try:
        _winreg.CreateKey(KEY_PATH, REG_PATH)
        registry_key = _winreg.OpenKey(KEY_PATH, REG_PATH, 0,
                                       _winreg.KEY_WRITE)
        _winreg.SetValueEx(registry_key, name, 0, _winreg.REG_SZ, value)
        _winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False

def get_env(name):
    """Get enviromental variable. """
    try:
        registry_key = _winreg.OpenKey(KEY_PATH, REG_PATH, 0,
                                       _winreg.KEY_READ)
        value, regtype = _winreg.QueryValueEx(registry_key, name)
        _winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None

