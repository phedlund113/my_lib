#
# pylint: disable=unused-wildcard-import, method-hidden
#

""" DocString Verifier for MyLib. """
from tkinter import *
from tkinter import ttk
from functools import partial
import os
import subprocess

import mylib.about
import mylib.box_char
import mylib.clock_face
import mylib.env
import mylib.data_validation
import mylib.file_log
import mylib.gage
import mylib.help
import mylib.knob
import mylib.led
import mylib.led_d
import mylib.led_sq
import mylib.low_ascii
import mylib.my_math
import mylib.p_types 
import mylib.print_colors
import mylib.scrn_log
import mylib.seven_seg
import mylib.sixteen_seg
import mylib.to_log
import mylib.SCRL_Notebook



prog_id = {'progname': 'doc_str_verify.py',
           'title': 'MyLib Doc String User Validator',
           'version': '1.3',
           'date': "11 December 2020",
           'rev_date': '16 July 2021',
           'author': "Peter Hedlund",
           'description': 'To test the doc Strings for all modules in the'
                          'mylib library.'}


def v_about():
    scrn.log_scrn_color('__ABOUT__\n', 'yellow')
    scrn.log_scrn(mylib.about.__doc__+'\n')
    scrn.log_scrn_color(mylib.about.get_full_lib_version() + '\n', 'blue')
    scrn.log_scrn_color('get_lib_version\n', 'cyan')
    scrn.log_scrn(mylib.about.get_lib_version.__doc__+'\n')
    scrn.log_scrn_color('get_full_lib_version\n', 'cyan')
    scrn.log_scrn(mylib.about.get_full_lib_version.__doc__+'\n')
    scrn.log_scrn_color('about_box\n', 'cyan')
    scrn.log_scrn(mylib.about.about_box.__doc__+'\n')


def v_box_char():
    scrn.log_scrn_color('__BOX_CHAR__\n', 'yellow')
    scrn.log_scrn( mylib.box_char.__doc__+'\n')
    rs = 'Library Name + ' + mylib.box_char.name_box_char + '\n'
    rs += 'Version : ' + mylib.box_char.version_box_char + '\n'
    rs += 'Date : ' + mylib.box_char.date_box_char + '\n'
    rs += 'Author : ' + mylib.box_char.author_box_char + '\n'
    scrn.log_scrn_color(rs, 'blue') 


def v_clock_face():
    scrn.log_scrn_color('__CLOCK_FACE__\n','yellow')
    scrn.log_scrn(mylib.clock_face.__doc__+'\n')
    # scrn.log_scrn_color(mylib.clock_face.my_clock.get_full_lib_version() + '\n', 'blue')
    scrn.log_scrn_color('get_lib_version\n', 'cyan')
    scrn.log_scrn(mylib.clock_face.my_clock.get_lib_version.__doc__+'\n')
    scrn.log_scrn_color('get_full_lib_version\n', 'cyan')
    scrn.log_scrn(mylib.clock_face.my_clock.get_full_lib_version.__doc__+'\n')
    scrn.log_scrn_color('my_clock\n', 'cyan')
    scrn.log_scrn(mylib.clock_face.my_clock.__doc__+'\n')
    scrn.log_scrn_color('show_time\n', 'cyan')
    scrn.log_scrn(mylib.clock_face.my_clock.show_time.__doc__+'\n')
    scrn.log_scrn_color('show_full_time\n', 'cyan')
    scrn.log_scrn(mylib.clock_face.my_clock.show_full_time.__doc__+'\n')


def v_env():
    scrn.log_scrn_color('__ENV__\n', 'yellow')
    scrn.log_scrn(mylib.env.__doc__+'\n')
    scrn.log_scrn_color(mylib.env.get_full_lib_version() + '\n', 'blue')
    scrn.log_scrn_color('get_lib_version\n', 'cyan')
    scrn.log_scrn(mylib.env.get_lib_version.__doc__+'\n')
    scrn.log_scrn_color('get_full_lib_version\n', 'cyan')
    scrn.log_scrn(mylib.env.get_full_lib_version.__doc__+'\n')
    scrn.log_scrn_color('set_env\n', 'cyan')
    scrn.log_scrn(mylib.env.set_env.__doc__+'\n')
    scrn.log_scrn_color('get_env\n', 'cyan')
    scrn.log_scrn(mylib.env.get_env.__doc__+'\n')

def v_data_validation():
    scrn.log_scrn_color('__DATA_VALIDATION__\n', 'yellow')
    scrn.log_scrn(mylib.data_validation.__doc__+'\n')
    scrn.log_scrn_color(mylib.data_validation.get_full_lib_version() + '\n', 'blue')
    scrn.log_scrn_color('get_lib_version\n', 'cyan')
    scrn.log_scrn(mylib.data_validation.get_lib_version.__doc__+'\n')
    scrn.log_scrn_color('get_full_lib_version\n', 'cyan')
    scrn.log_scrn(mylib.data_validation.get_full_lib_version.__doc__+'\n')
    scrn.log_scrn_color('checksum_8\n', 'cyan')
    scrn.log_scrn(mylib.data_validation.checksum_8.__doc__+'\n')
    scrn.log_scrn_color('checksum_16\n', 'cyan')
    scrn.log_scrn(mylib.data_validation.checksum_16.__doc__+'\n')
    scrn.log_scrn_color('crc16\n', 'cyan')
    scrn.log_scrn(mylib.data_validation.crc16.__doc__+'\n')
    scrn.log_scrn_color('crc16_CCITT\n', 'cyan')
    scrn.log_scrn(mylib.data_validation.crc16_CCITT.__doc__+'\n')

def v_file_log():
    scrn.log_scrn_color('__FILE_LOG__\n', 'yellow')
    scrn.log_scrn( mylib.file_log.__doc__+'\n')
    tst = mylib.file_log.file_log('','',0)
    scrn.log_scrn_color(tst.get_full_lib_version() + '\n', 'blue')
    scrn.log_scrn_color( 'get_lib_version\n', 'cyan')
    scrn.log_scrn( mylib.file_log.file_log.get_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'get_full_lib_version\n', 'cyan')
    scrn.log_scrn( mylib.file_log.file_log.get_full_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'log\n', 'cyan')
    scrn.log_scrn( mylib.file_log.file_log.log.__doc__+'\n')
    scrn.log_scrn_color( 'log_dt\n', 'cyan')
    scrn.log_scrn( mylib.file_log.file_log.log_dt.__doc__+'\n')
    scrn.log_scrn_color( 'header\n', 'cyan')
    scrn.log_scrn( mylib.file_log.file_log.header.__doc__+'\n')


def v_gage():
    scrn.log_scrn_color('__GAGE__\n', 'yellow')
    scrn.log_scrn( mylib.gage.__doc__+'\n')
    scrn.log_scrn_color('get_lib_version\n', 'cyan')
    scrn.log_scrn( mylib.gage.gage.get_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'get_full_lib_version\n', 'cyan')
    scrn.log_scrn( mylib.gage.gage.get_full_lib_version.__doc__+'\n')
    # scrn.log_scrn_color(mylib.gage.get_full_lib_version() + '\n', 'blue')
    scrn.log_scrn_color( 'Gage\n', 'cyan')
    scrn.log_scrn( mylib.gage.gage.__doc__+'\n')
    scrn.log_scrn_color( 'draw_value\n', 'cyan')
    scrn.log_scrn( mylib.gage.gage.draw_value.__doc__+'\n')


def v_help():
    scrn.log_scrn_color('__HELP__\n', 'yellow')
    scrn.log_scrn( mylib.help.__doc__+'\n')
    scrn.log_scrn_color( 'Full Version : ' + 
           mylib.help.get_full_lib_version() + '\n', 'blue')
    scrn.log_scrn_color( 'get_lib_version\n', 'cyan')
    scrn.log_scrn( mylib.help.get_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'get_full_lib_version\n', 'cyan')
    scrn.log_scrn( mylib.help.get_full_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'Dialog\n', 'cyan')
    scrn.log_scrn( mylib.help.Dialog.__doc__+'\n')


def v_knob():
    scrn.log_scrn_color('__KNOB__\n', 'yellow')
    scrn.log_scrn( mylib.knob.__doc__+'\n')
    scrn.log_scrn_color( 'get_lib_version\n', 'cyan')
    scrn.log_scrn( mylib.knob.knob.get_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'get_full_lib_version\n', 'cyan')
    scrn.log_scrn( mylib.knob.knob.get_full_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'Gage\n', 'cyan')
    scrn.log_scrn( mylib.knob.knob.__doc__+'\n')
    scrn.log_scrn_color( 'show_angle\n', 'cyan')
    scrn.log_scrn( mylib.knob.knob.show_angle.__doc__+'\n')
    scrn.log_scrn_color( 'get_knob\n', 'cyan')
    scrn.log_scrn( mylib.knob.knob.get_knob.__doc__+'\n')
    scrn.log_scrn_color( 'draw_value\n', 'cyan')
    scrn.log_scrn( mylib.knob.knob.draw_value.__doc__+'\n')


def v_led_d():
    scrn.log_scrn_color('__LED_D__\n', 'yellow')
    scrn.log_scrn( mylib.led_d.__doc__+'\n')
    scrn.log_scrn_color( 'Full Version : ' + 
            mylib.led_d.get_full_lib_version() + '\n', 'blue')
    scrn.log_scrn_color( 'get_lib_version\n', 'cyan')
    scrn.log_scrn( mylib.led_d.get_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'get_full_lib_version\n', 'cyan')
    scrn.log_scrn( mylib.led_d.get_full_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'make_led_dr\n', 'cyan')
    scrn.log_scrn( mylib.led_d.make_led_dr.__doc__+'\n')
    scrn.log_scrn_color( 'make_led_ds\n', 'cyan')
    scrn.log_scrn( mylib.led_d.make_led_ds.__doc__+'\n')
    scrn.log_scrn_color( 'set_led\n', 'cyan')
    scrn.log_scrn( mylib.led_d.set_led.__doc__+'\n')
    scrn.log_scrn_color( 'get_led\n', 'cyan')
    scrn.log_scrn( mylib.led_d.get_led.__doc__+'\n')


def v_led_r():
    scrn.log_scrn_color('__LED_R__\n', 'yellow')
    scrn.log_scrn( mylib.led.__doc__+'\n')
    scrn.log_scrn_color( 'Full Version : ' + 
            mylib.led.get_full_lib_version() + '\n', 'blue')
    scrn.log_scrn_color( 'get_lib_version\n', 'cyan')
    scrn.log_scrn( mylib.led.get_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'get_full_lib_version\n', 'cyan')
    scrn.log_scrn( mylib.led.get_full_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'make_led_1r\n', 'cyan')
    scrn.log_scrn( mylib.led.make_led_1r.__doc__+'\n')
    scrn.log_scrn_color( 'set_led_1r\n', 'cyan')
    scrn.log_scrn( mylib.led.set_led_1r.__doc__+'\n')
    scrn.log_scrn_color( 'get_led_1r\n', 'cyan')
    scrn.log_scrn( mylib.led.get_led_1r.__doc__+'\n')
    scrn.log_scrn_color( 'make_led_2r\n', 'cyan')
    scrn.log_scrn( mylib.led.make_led_2r.__doc__+'\n')
    scrn.log_scrn_color( 'make_led_4r\n', 'cyan')
    scrn.log_scrn( mylib.led.make_led_4r.__doc__+'\n')
    scrn.log_scrn_color( 'make_led_8r\n', 'cyan')
    scrn.log_scrn( mylib.led.make_led_8r.__doc__+'\n')
    scrn.log_scrn_color( 'led2num_2r\n', 'cyan')
    scrn.log_scrn( mylib.led.led2num_2r.__doc__+'\n')
    scrn.log_scrn_color( 'led2num_4r\n', 'cyan')
    scrn.log_scrn( mylib.led.led2num_4r.__doc__+'\n')
    scrn.log_scrn_color( 'led2num_8r\n', 'cyan')
    scrn.log_scrn( mylib.led.led2num_8r.__doc__+'\n')
    scrn.log_scrn_color( 'set_leds_r\n', 'cyan')
    scrn.log_scrn( mylib.led.set_leds_r.__doc__+'\n')
    scrn.log_scrn_color( 'get_leds_r\n', 'cyan')
    scrn.log_scrn( mylib.led.get_leds_r.__doc__+'\n')


def v_led_s():
    scrn.log_scrn_color('__LED_S__\n', 'yellow')
    scrn.log_scrn( mylib.led_sq.__doc__+'\n')
    scrn.log_scrn_color( 'Full Version : ' + 
            mylib.led_sq.get_full_lib_version() + '\n', 'blue')
    scrn.log_scrn_color( 'get_lib_version\n', 'cyan')
    scrn.log_scrn( mylib.led_sq.get_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'get_full_lib_version\n', 'cyan')
    scrn.log_scrn( mylib.led_sq.get_full_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'make_led_1s\n', 'cyan')
    scrn.log_scrn( mylib.led_sq.make_led_1s.__doc__+'\n')
    scrn.log_scrn_color( 'set_led_1s\n', 'cyan')
    scrn.log_scrn( mylib.led_sq.set_led_1s.__doc__+'\n')
    scrn.log_scrn_color( 'get_led_1s\n', 'cyan')
    scrn.log_scrn( mylib.led_sq.get_led_1s.__doc__+'\n')
    scrn.log_scrn_color( 'make_led_2s\n', 'cyan')
    scrn.log_scrn( mylib.led_sq.make_led_2s.__doc__+'\n')
    scrn.log_scrn_color( 'make_led_4s\n', 'cyan')
    scrn.log_scrn( mylib.led_sq.make_led_4s.__doc__+'\n')
    scrn.log_scrn_color( 'make_led_8s\n', 'cyan')
    scrn.log_scrn( mylib.led_sq.make_led_8s.__doc__+'\n')
    scrn.log_scrn_color( 'led2num_2s\n', 'cyan')
    scrn.log_scrn( mylib.led_sq.led2num_2s.__doc__+'\n')
    scrn.log_scrn_color( 'led2num_4s\n', 'cyan')
    scrn.log_scrn( mylib.led_sq.led2num_4s.__doc__+'\n')
    scrn.log_scrn_color( 'led2num_8s\n', 'cyan')
    scrn.log_scrn( mylib.led_sq.led2num_8s.__doc__+'\n')
    scrn.log_scrn_color( 'set_leds_s\n', 'cyan')
    scrn.log_scrn( mylib.led_sq.set_leds_s.__doc__+'\n')
    scrn.log_scrn_color( 'get_leds_s\n', 'cyan')
    scrn.log_scrn( mylib.led_sq.get_leds_s.__doc__+'\n')


def v_low_ascii():
    scrn.log_scrn_color('__LOW_ASCII__\n', 'yellow')
    scrn.log_scrn( mylib.low_ascii.__doc__+'\n')
    rs = 'Library Name + ' + mylib.low_ascii.name_low_ascii + '\n'
    rs += 'Version : ' + mylib.low_ascii.version_low_ascii + '\n'
    rs += 'Date : ' + mylib.low_ascii.date_low_ascii + '\n'
    rs += 'Author : ' + mylib.low_ascii.author_low_ascii + '\n'
    scrn.log_scrn_color(rs, 'blue') 


def v_my_math():
    scrn.log_scrn_color('__MY_MATH__\n', 'yellow')
    scrn.log_scrn( mylib.my_math.__doc__+'\n')
    scrn.log_scrn_color(mylib.my_math.get_full_lib_version() + '\n', 'blue')
    scrn.log_scrn_color( 'get_lib_version\n', 'cyan')
    scrn.log_scrn( mylib.my_math.get_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'get_full_lib_version\n', 'cyan')
    scrn.log_scrn( mylib.my_math.get_full_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'inside\n', 'cyan')
    scrn.log_scrn( mylib.my_math.inside.__doc__+'\n')
    scrn.log_scrn_color( 'outside\n', 'cyan')
    scrn.log_scrn( mylib.my_math.outside.__doc__+'\n')
    scrn.log_scrn_color( 're_scale\n', 'cyan')
    scrn.log_scrn( mylib.my_math.re_scale.__doc__+'\n')
    scrn.log_scrn_color('sec_2_hms\n', 'cyan')
    scrn.log_scrn( mylib.my_math.sec_2_hms.__doc__+'\n')
    scrn.log_scrn_color('Current_time\n', 'cyan')
    scrn.log_scrn( mylib.my_math.current_time.__doc__+'\n')
    scrn.log_scrn_color( 'filter_float\n', 'cyan')
    scrn.log_scrn( mylib.my_math.filter_float.__doc__+'\n')


def v_p_types():
    scrn.log_scrn_color('__P_TYPES__\n', 'yellow')
    scrn.log_scrn( mylib.p_types.__doc__+'\n')
    rs = 'Library Name + ' + mylib.p_types.name_p_types + '\n'
    rs += 'Version : ' + mylib.p_types.version_p_types + '\n'
    rs += 'Date : ' + mylib.p_types.date_p_types + '\n'
    rs += 'Author : ' + mylib.p_types.author_p_types + '\n'
    scrn.log_scrn_color(rs, 'blue') 

def v_print_colors():
    scrn.log_scrn_color('__PRINT_COLORS__\n', 'yellow')
    scrn.log_scrn( mylib.print_colors.__doc__+'\n')
    rs = 'Library Name + ' + mylib.print_colors.name_print_colors + '\n'
    rs += 'Version : ' + mylib.print_colors.version_print_colors + '\n'
    rs += 'Date : ' + mylib.print_colors.date_print_colors + '\n'
    rs += 'Author : ' + mylib.print_colors.author_print_colors + '\n'
    scrn.log_scrn_color(rs, 'blue') 
    scrn.log_scrn_color( 'pr_cursor_up\n', 'cyan')
    scrn.log_scrn( mylib.print_colors.pr_cursor_up.__doc__+'\n')
    scrn.log_scrn_color( 'pr_cursor_down\n', 'cyan')
    scrn.log_scrn( mylib.print_colors.pr_cursor_down.__doc__+'\n')
    scrn.log_scrn_color( 'pr_cursor_forward\n', 'cyan')
    scrn.log_scrn( mylib.print_colors.pr_cursor_forward.__doc__+'\n')
    scrn.log_scrn_color( 'pr_cursor_back\n', 'cyan')
    scrn.log_scrn( mylib.print_colors.pr_cursor_back.__doc__+'\n')
    scrn.log_scrn_color( 'pr_cursor_next_ln\n', 'cyan')
    scrn.log_scrn( mylib.print_colors.pr_cursor_next_ln.__doc__+'\n')
    scrn.log_scrn_color( 'pr_cursor_prev_ln\n', 'cyan')
    scrn.log_scrn( mylib.print_colors.pr_cursor_prev_ln.__doc__+'\n')
    scrn.log_scrn_color( 'pr_cursor_horiz\n', 'cyan')
    scrn.log_scrn( mylib.print_colors.pr_cursor_horiz.__doc__+'\n')
    scrn.log_scrn_color( 'pr_cursor_pos\n', 'cyan')
    scrn.log_scrn( mylib.print_colors.pr_cursor_pos.__doc__+'\n')
    scrn.log_scrn_color( 'pr_erase_in_dsp\n', 'cyan')
    scrn.log_scrn( mylib.print_colors.pr_erase_in_dsp.__doc__+'\n')
    scrn.log_scrn_color( 'pr_erase_in_line\n', 'cyan')
    scrn.log_scrn( mylib.print_colors.pr_erase_in_line.__doc__+'\n')
    scrn.log_scrn_color( 'pr_scroll_up\n', 'cyan')
    scrn.log_scrn( mylib.print_colors.pr_scroll_up.__doc__+'\n')
    scrn.log_scrn_color( 'pr_scroll_down\n', 'cyan')
    scrn.log_scrn( mylib.print_colors.pr_scroll_down.__doc__+'\n')
    scrn.log_scrn_color( 'pr_cursor_save\n', 'cyan')
    scrn.log_scrn( mylib.print_colors.pr_cursor_save.__doc__+'\n')
    scrn.log_scrn_color( 'pr_corsor_restore\n', 'cyan')
    scrn.log_scrn( mylib.print_colors.pr_corsor_restore.__doc__+'\n')
    scrn.log_scrn_color( 'pr_cursor_show\n', 'cyan')
    scrn.log_scrn( mylib.print_colors.pr_cursor_show.__doc__+'\n')
    scrn.log_scrn_color( 'pr_cursor_hide\n', 'cyan')
    scrn.log_scrn( mylib.print_colors.pr_cursor_hide.__doc__+'\n')


def v_scrl_notebook():
    scrn.log_scrn_color('__Scrollable_Notebook__\n', 'yellow')
    scrn.log_scrn( sn.__doc__+'\n')
    scrn.log_scrn_color(sn.get_full_lib_version() + '\n', 'blue')
    scrn.log_scrn_color( 'get_lib_version\n', 'cyan')
    scrn.log_scrn( sn.get_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'get_full_lib_version\n', 'cyan')
    scrn.log_scrn( sn.get_full_lib_version.__doc__+'\n')


def v_scrn_log():
    scrn.log_scrn_color('__SCRN_LOG__\n', 'yellow')
    scrn.log_scrn( scrn.__doc__+'\n')
    scrn.log_scrn_color( 'Full Version : ' + 
           scrn.get_full_lib_version() + '\n', 'blue')
    scrn.log_scrn_color( 'get_lib_version\n', 'cyan')
    scrn.log_scrn( scrn.get_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'get_full_lib_version\n', 'cyan')
    scrn.log_scrn( scrn.get_full_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'log_scrn\n', 'cyan')
    scrn.log_scrn( scrn.log_scrn.__doc__+'\n')
    scrn.log_scrn_color( 'log_scrn_color\n', 'cyan')
    scrn.log_scrn( scrn.log_scrn_color.__doc__+'\n')
    scrn.log_scrn_color( 'log_scrn_raw\n', 'cyan')
    scrn.log_scrn( scrn.log_scrn_raw.__doc__+'\n')
    scrn.log_scrn_color( 'get_pos\n', 'cyan')
    scrn.log_scrn( scrn.get_pos.__doc__+'\n')
    scrn.log_scrn_color( 'clear_scrn\n', 'cyan')
    scrn.log_scrn( scrn.clear_scrn.__doc__+'\n')
    scrn.log_scrn_color( 'save_scrn\n', 'cyan')
    scrn.log_scrn( scrn.save_scrn.__doc__+'\n')
    scrn.log_scrn_color( 'clipboard_scrn\n', 'cyan')
    scrn.log_scrn( scrn.clipboard_scrn.__doc__+'\n')


def v_seven_seg():
    scrn.log_scrn_color('__SEVEN_SEG__\n', 'yellow')
    scrn.log_scrn( mylib.seven_seg.__doc__+'\n')
    scrn.log_scrn_color( 'Full Version : ' + 
            mylib.seven_seg.get_full_lib_version() + '\n', 'blue')
    scrn.log_scrn_color( 'get_lib_version\n', 'cyan')
    scrn.log_scrn( mylib.seven_seg.get_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'get_full_lib_version\n', 'cyan')
    scrn.log_scrn( mylib.seven_seg.get_full_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'Digit\n', 'cyan')
    scrn.log_scrn( mylib.seven_seg.Digit.__doc__+'\n')
    scrn.log_scrn_color( 'Digit.show\n', 'cyan')
    scrn.log_scrn( mylib.seven_seg.Digit.show.__doc__+'\n')
    scrn.log_scrn_color( 'Counter\n', 'cyan')
    scrn.log_scrn( mylib.seven_seg.Counter.__doc__+'\n')
    scrn.log_scrn_color( 'Counter.num\n', 'cyan')
    scrn.log_scrn( mylib.seven_seg.Counter.num.__doc__+'\n')
    scrn.log_scrn_color( 'Counter_Dp\n', 'cyan')
    scrn.log_scrn( mylib.seven_seg.Counter_Dp.__doc__+'\n')
    scrn.log_scrn_color( 'Counter_Dp.num\n', 'cyan')
    scrn.log_scrn( mylib.seven_seg.Counter_Dp.num.__doc__+'\n')
    scrn.log_scrn_color( 'Digit_Led\n', 'cyan')
    scrn.log_scrn( mylib.seven_seg.Digit_Led.__doc__+'\n')
    scrn.log_scrn_color( 'Digit_Led.show\n', 'cyan')
    scrn.log_scrn( mylib.seven_seg.Digit_Led.show.__doc__+'\n')
    scrn.log_scrn_color( 'Counter_Led\n', 'cyan')
    scrn.log_scrn( mylib.seven_seg.Counter_Led.__doc__+'\n')
    scrn.log_scrn_color( 'Counter_Led.num\n', 'cyan')
    scrn.log_scrn( mylib.seven_seg.Counter_Led.num.__doc__+'\n')
    scrn.log_scrn_color( 'Counter_Led_Dp\n', 'cyan')
    scrn.log_scrn( mylib.seven_seg.Counter_Led_Dp.__doc__+'\n')
    scrn.log_scrn_color( 'Counter_Led_Dp.num\n', 'cyan')
    scrn.log_scrn( mylib.seven_seg.Counter_Led_Dp.num.__doc__+'\n')


def v_16_seg():
    scrn.log_scrn_color('__SIXTEEN_SEG__\n', 'yellow')
    scrn.log_scrn( mylib.sixteen_seg.__doc__+'\n')
    scrn.log_scrn_color( 'Full Version : ' + 
            mylib.sixteen_seg.get_full_lib_version() + '\n', 'blue')
    scrn.log_scrn_color( 'get_lib_version\n', 'cyan')
    scrn.log_scrn( mylib.sixteen_seg.get_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'get_full_lib_version\n', 'cyan')
    scrn.log_scrn( mylib.sixteen_seg.get_full_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'seg16Digit\n', 'cyan')
    scrn.log_scrn( mylib.sixteen_seg.seg16Digit.__doc__+'\n')
    scrn.log_scrn_color( 'seg16Digit.show\n', 'cyan')
    scrn.log_scrn( mylib.sixteen_seg.seg16Digit.show.__doc__+'\n')
    scrn.log_scrn_color( 'StrDisp\n', 'cyan')
    scrn.log_scrn( mylib.sixteen_seg.StrDisp.__doc__+'\n')
    scrn.log_scrn_color( 'StrDisp.show\n', 'cyan')
    scrn.log_scrn( mylib.sixteen_seg.StrDisp.show.__doc__+'\n')


def v_to_log():
    scrn.log_scrn_color('__to_log__\n', 'yellow')
    scrn.log_scrn( scrn.log_scrn.__doc__+'\n')
    scrn.log_scrn_color('For Legacy Code only --- use scrn_log module\n','red')
    scrn.log_scrn_color( 'Full Version : ' + 
           mylib.to_log.get_full_lib_version() + '\n', 'blue')
    scrn.log_scrn_color( 'get_lib_version\n', 'cyan')
    scrn.log_scrn( mylib.to_log.get_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'get_full_lib_version\n', 'cyan')
    scrn.log_scrn( mylib.to_log.get_full_lib_version.__doc__+'\n')
    scrn.log_scrn_color( 'to_log\n', 'cyan')
    scrn.log_scrn( mylib.to_log.to_log.__doc__+'\n')
    scrn.log_scrn_color( 'to_log_red\n', 'cyan')
    scrn.log_scrn( mylib.to_log.to_log_red.__doc__+'\n')
    scrn.log_scrn_color( 'to_log_blue\n', 'cyan')
    scrn.log_scrn( mylib.to_log.to_log_blue.__doc__+'\n')
    scrn.log_scrn_color( 'to_log_green\n', 'cyan')
    scrn.log_scrn( mylib.to_log.to_log_green.__doc__+'\n')
    scrn.log_scrn_color( 'to_log_yellow\n', 'cyan')
    scrn.log_scrn( mylib.to_log.to_log_yellow.__doc__+'\n')
    scrn.log_scrn_color( 'to_log_cyan\n', 'cyan')
    scrn.log_scrn( mylib.to_log.to_log_cyan.__doc__+'\n')
    scrn.log_scrn_color( 'to_log_white\n', 'cyan')
    scrn.log_scrn( mylib.to_log.to_log_white.__doc__+'\n')
    scrn.log_scrn_color( 'to_log_violet\n', 'cyan')
    scrn.log_scrn( mylib.to_log.to_log_violet.__doc__+'\n')
    scrn.log_scrn_color( 'clear_log\n', 'cyan')
    scrn.log_scrn( mylib.to_log.clear_log.__doc__+'\n')
    scrn.log_scrn_color( 'save_log\n', 'cyan')
    scrn.log_scrn( mylib.to_log.save_log.__doc__+'\n')


def run_button(strx):
    subprocess.call("%s %s" % ('python', strx))


def my_clear_log():
    scrn.clear_scrn()


def my_about_box(event=None):
    mylib.about.about_box(prog_id)


def quit_prog():
    root.destroy()

my_data = (
    # Verify       | enable | button Name      | program to run
    (v_about,           1,  'About',           'about.py'),
    (v_box_char,        1,  'Box Characters',  'box_char.py'),
    (v_clock_face,      1,  'Clock Face',      'clock_face.py'),
    (v_data_validation, 1,  'Data Validate',   'data_validation.py'),
    (v_env,             0,  'Enviorment',      'env.py'),
    (v_file_log,        1,  'File Logging',    'file_log.py'),
    (v_gage,            1,  'Gage',            'gage.py'),
    (v_help,            1,  'Help',            'help.py'),
    (v_knob,            1,  'Knob',            'knob.py'),
    (v_led_d,           1,  'Dual Leds',       'led_d.py'),
    (v_led_r,           1,  'Round Leds',      'led.py'),
    (v_led_s,           1,  'Square Leds',     'led_sq.py'),
    (v_low_ascii,       0,  'Low Ascii',       'low_ascii.py'),
    (v_my_math,         1,  'My Math',         'my_math.py'),
    (v_p_types,         0,  'P Types',         'p_types.py'),
    (v_print_colors,    0,  'Print Colors',    'print_colors.py'),
    (v_scrl_notebook,   1,  'Scroll Notebook', 'scrl_notebook.py'),
    (v_scrn_log,        1,  'Screen Log',      'scrn_log.py'),
    (v_seven_seg,       1,  'Seven Segment',   'seven_seg.py'),
    (v_16_seg,          1,  '16 Segment',      'sixteen_seg.py'),
    (v_to_log,          1,  'To Log',          'to_log.py'),
)

root = Tk()
root.resizable(0,0)
root.title(prog_id['title']+'      Version : '+prog_id['version'])
mainframe = ttk.Frame(root, padding='3', height=780, width=870)
mainframe.grid(column=1, row=2, sticky=(N, W, E, S))
mainframe.grid_propagate(0)
root.protocol("WM_DELETE_WINDOW", quit_prog)
ln = len(my_data)
for x in range(0,ln):
    btn = ttk.Button(mainframe, text=my_data[x][2], command=my_data[x][0])
    btn.grid(column=0, row=x+2)
    if my_data[x][1] == 1:
        btn = ttk.Button(mainframe, text='Test Program', 
                         command=partial(run_button, my_data[x][3]))
        btn.grid(column=1, row=x+2)
ab = ttk.Button(mainframe, text='About', command=my_about_box)
ab.grid(column=2, row=23)
ab = ttk.Button(mainframe, text='Clear', command=my_clear_log)
ab.grid(column=3, row=23)
ab = ttk.Button(mainframe, text='Quit', command=quit_prog)
ab.grid(column=4, row=23)

## ------------------------------------
##  Text box Widget
## ------------------------------------

scrn = mylib.scrn_log.scrn_log(mainframe, 80, 34, 'lightgreen', 'black', 2, 0, 6, 22)
sn = mylib.SCRL_Notebook.ScrollableNotebook(mainframe)
sn.grid(column=1, row=10)
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
