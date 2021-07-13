# box_char.py

"""Character defnitions for ascii box characters"""
name_box_char    = 'box_char.py'
version_box_char = '1.2.0'
date_box_char    = '04/30/21'
author_box_char  = 'Peter A. Hedlund'

# Single Line box
h_bar_     = '\u2500'   # horizontal bar 1 char wide
v_bar_     = '\u2502'   # Vertical Bar 1 char tall
ul_corner_ = '\u250c'   # upper left corner
ur_corner_ = '\u2510'   # upper right corner
ll_corner_ = '\u2514'   # Lower left corner
lr_corner_ = '\u2518'   # lower right corner
v_bar_tr_  = '\u251c'   # Vertical bar split right
v_bar_tl_  = '\u2524'   # Vertical bar split left
h_bar_td_  = '\u252c'   # Horizontal bar split up
h_bar_tu_  = '\u2534'   # horizontal bar split down
ctr_cross_ = '\u253c'   # center cross (vertical and horizontal bar)

# Double Line Box
dl_h_bar_  = '\u2550'   # horizontal bar 1 char wide
dl_v_bar_  = '\u2551'   # Vertical Bar 1 char tall
dl_ul_c_   = '\u2554'   # upper left corner
dl_ur_c_   = '\u2557'   # upper right corner
dl_ll_c_   = '\u255a'   # Lower left corner
dl_lr_c_   = '\u255d'   # lower right corner
dl_vb_tr_  = '\u2560'   # Vertical bar split right
dl_vb_tl_  = '\u2563'   # Vertical bar split left
dl_hb_tu_  = '\u2569'   # Horizontal bar split up
dl_hb_td_  = '\u2566'   # horizontal bar split down
dl_cross_  = '\u256c'   # center cross (vertical and horizontal bar)
# Double Hozizontal
dh_ul_c_   = '\u2552'   # upper left corner
dh_ur_c_   = '\u2555'   # upper right corner
dh_ll_c_   = '\u2558'   # Lower left corner
dh_lr_c_   = '\u255b'   # lower right corner
dh_vb_tr_  = '\u255e'   # Vertical bar split right
dh_vb_tl_  = '\u2561'   # Vertical bar split left
dh_hb_tu_  = '\u2567'   # Horizontal bar split up
dh_hb_td_  = '\u2564'   # horizontal bar split down
dh_cross_  = '\u256a'   # center cross (vertical and horizontal bar)
# Double Vertical
dv_ul_c_   = '\u2553'   # upper left corner
dv_ur_c_   = '\u2556'   # upper right corner
dv_ll_c_   = '\u2559'   # Lower left corner
dv_lr_c_   = '\u255c'   # lower right corner
dv_vb_tr_  = '\u255f'   # Vertical bar split right
dv_vb_tl_  = '\u2562'   # Vertical bar split left
dv_hb_tu_  = '\u2568'   # Horizontal bar split up
dv_hb_td_  = '\u2565'   # horizontal bar split down
dv_cross_  = '\u256b'   # center cross (vertical and horizontal bar)

if __name__ == "__main__":
    from tkinter import *
    from tkinter import ttk
    import mylib.scrn_log as scrn

    def send_str(txt, wstr):
        txt.insert(END,wstr)
        txt.index(END)
        txt.see(END)
        txt.update()

    root = Tk()
    #  prevent window resizing.
    root.resizable(0, 0)
    # Replace tk icon with your own.
    root.title('Box Characters DEMO')
    mainframe = ttk.Frame(root, padding="3", height=340, width=440)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.grid_propagate(0)

    log = scrn.scrn_log(mainframe, 50, 20, 'black', 'light grey', 0, 0, 2, 10)

    log.log_scrn('Box Char Library Test\n')
    log.log_scrn(f'Small Box  {ul_corner_}{ur_corner_}\n')
    log.log_scrn(f'           {ll_corner_}{lr_corner_}\n')

    log.log_scrn(f'           {ul_corner_}{h_bar_}{ur_corner_}\n')
    log.log_scrn(f'Medium Box {v_bar_}X{v_bar_}\n')
    log.log_scrn(f'           {ll_corner_}{h_bar_}{lr_corner_}\n')

    log.log_scrn(f'           {ul_corner_}{h_bar_td_}{ur_corner_}\n')
    log.log_scrn(f'4 pane Box {v_bar_tr_}{ctr_cross_}{v_bar_tl_}\n')
    log.log_scrn(f'           {ll_corner_}{h_bar_tu_}{lr_corner_}\n')

    log.log_scrn(f'           {ul_corner_}{h_bar_}{h_bar_td_}{h_bar_}{ur_corner_}\n')
    log.log_scrn(f'4 pane Box {v_bar_tr_}{h_bar_}{ctr_cross_}{h_bar_}{v_bar_tl_}\n')
    log.log_scrn(f'           {ll_corner_}{h_bar_}{h_bar_tu_}{h_bar_}{lr_corner_}\n')

    log.log_scrn(f'           {ul_corner_}{h_bar_}{h_bar_td_}{h_bar_}{ur_corner_}\n')
    log.log_scrn(f'4 pane Box {v_bar_}X{v_bar_}X{v_bar_}\n')
    log.log_scrn(f'single     {v_bar_tr_}{h_bar_}{ctr_cross_}{h_bar_}{v_bar_tl_}\n')
    log.log_scrn(f'           {v_bar_}X{v_bar_}X{v_bar_}\n')
    log.log_scrn(f'           {ll_corner_}{h_bar_}{h_bar_tu_}{h_bar_}{lr_corner_}\n')

    log.log_scrn(f'           {dl_ul_c_}{dl_h_bar_}{dl_hb_td_}{dl_h_bar_}{dl_ur_c_}\n')
    log.log_scrn(f'4 pane Box {dl_v_bar_}X{dl_v_bar_}X{dl_v_bar_}\n')
    log.log_scrn(f'double     {dl_vb_tr_}{dl_h_bar_}{dl_cross_}{dl_h_bar_}{dl_vb_tl_}\n')
    log.log_scrn(f'           {dl_v_bar_}X{dl_v_bar_}X{dl_v_bar_}\n')
    log.log_scrn(f'           {dl_ll_c_}{dl_h_bar_}{dl_hb_tu_}{dl_h_bar_}{dl_lr_c_}\n')

    log.log_scrn(f'           {dh_ul_c_}{dl_h_bar_}{dh_hb_td_}{dl_h_bar_}{dh_ur_c_}\n')
    log.log_scrn(f'4 pane Box {v_bar_}X{v_bar_}X{v_bar_}\n')
    log.log_scrn(f'dbl horiz  {dh_vb_tr_}{dl_h_bar_}{dh_cross_}{dl_h_bar_}{dh_vb_tl_}\n')
    log.log_scrn(f'           {v_bar_}X{v_bar_}X{v_bar_}\n')
    log.log_scrn(f'           {dh_ll_c_}{dl_h_bar_}{dh_hb_tu_}{dl_h_bar_}{dh_lr_c_}\n')

    log.log_scrn(f'           {dv_ul_c_}{h_bar_}{dv_hb_td_}{h_bar_}{dv_ur_c_}\n')
    log.log_scrn(f'4 pane Box {dl_v_bar_}X{dl_v_bar_}X{dl_v_bar_}\n')
    log.log_scrn(f'dbl vert   {dv_vb_tr_}{h_bar_}{dv_cross_}{h_bar_}{dv_vb_tl_}\n')
    log.log_scrn(f'           {dl_v_bar_}X{dl_v_bar_}X{dl_v_bar_}\n')
    log.log_scrn(f'           {dv_ll_c_}{h_bar_}{dv_hb_tu_}{h_bar_}{dv_lr_c_}\n')

    
    
    
    for child in root.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()



 