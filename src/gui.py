THEME_FILE = 'config/theme.txt'
NAME_FILE = 'config/name.txt'
COVER_FILE = 'media/not_connected.png'

import vpn

import os
import tkinter
import webbrowser
import tkinter.messagebox

from PIL import ImageTk, Image

if not os.path.exists(THEME_FILE):
    open(THEME_FILE, 'w').write('light')

if not os.path.exists(NAME_FILE):
    open(NAME_FILE, 'w').write('Lix')

def theme():
    if open(THEME_FILE).read() == 'dark':
        return {
            'fg': 'white',
            'bg': '#0E0F13',
            'light': '#008AE6',
            'hover': '#655bdb',
            'warn': '#fc9d19',
            'critical': '#fc3b19',
            'ok': '#28ff02'
        }
    else:
        return {
            'fg': 'black',
            'bg': 'white',
            'light': '#008AE6',
            'hover': '#655bdb',
            'warn': '#fc9d19',
            'critical': '#fc3b19',
            'ok': '#28ff02'
        }        

def vpn_name():
    return open(NAME_FILE).read()

def font_type():
    return 'Yu Gothic' if os.name == 'nt' else 'URW Gothic' 

def theme_toggle():
    if open(THEME_FILE).read() == 'light':
        open(THEME_FILE, 'w').write('dark')
    else:
        open(THEME_FILE, 'w').write('light')

    if tkinter.messagebox.askyesno(title='Theme Toggle', message='The changes will apply after restarting.\nExit program now? (You need to start the program again for yourself.'):
        exit()

def open_info():
    webbrowser.open('https://github.com/nsde/lixvpn')

def separator(space=5):
    tkinter.Label(win, text='\n'*space, font=(font_type(), 5), fg=theme()['bg'], bg=theme()['bg']).pack()

def connect():
    vpn.connect()

win = tkinter.Tk()
win.config(bg=theme()['bg'])
win.title(f'{vpn_name()}VPN')
win.geometry('700x600')

cover_image = ImageTk.PhotoImage(Image.open(COVER_FILE))
tkinter.Button(win, image=cover_image, height=170, relief='flat', overrelief='flat', borderwidth=0, padx=0, pady=0, highlightthickness=0, bg=theme()['bg'], cursor='hand2', activeforeground=theme()['hover'], activebackground=theme()['bg']).pack()

separator(1)

title_row = tkinter.Frame(win, width=900, relief='flat', bd=0, bg=theme()['bg'], background=theme()['bg'], borderwidth=0)
title_row.pack()

tkinter.Label(title_row, text='Available VPNs:', font=(font_type(), 25), fg=theme()['fg'], bg=theme()['bg']).pack(side='left')
separator(1)

for v in vpn.vpns():
    tkinter.Button(win, text=f'· {v.title().split(".")[0]}', command=lambda v=v: vpn.connect(v), font=(font_type(), 25, 'bold'), fg=theme()['fg'], bg=theme()['bg'], relief='flat', overrelief='flat', borderwidth=0, highlightthickness=0, padx=0, pady=0, cursor='hand2', activeforeground=theme()['hover'], activebackground=theme()['bg']).pack()

separator(1)
tkinter.Button(win, text='VPN Shop', command=vpn.show_shop, font=(font_type(), 20), fg=theme()['light'], bg=theme()['bg'], relief='flat', overrelief='flat', borderwidth=0, highlightthickness=0, padx=0, pady=0, cursor='hand2', activeforeground=theme()['hover'], activebackground=theme()['bg']).pack()
tkinter.Button(win, text='How to add a VPN', command=vpn.show_tutorial, font=(font_type(), 20), fg=theme()['light'], bg=theme()['bg'], relief='flat', overrelief='flat', borderwidth=0, highlightthickness=0, padx=0, pady=0, cursor='hand2', activeforeground=theme()['hover'], activebackground=theme()['bg']).pack()
tkinter.Button(win, text='Log', command=vpn.show_log, font=(font_type(), 20), fg=theme()['light'], bg=theme()['bg'], relief='flat', overrelief='flat', borderwidth=0, highlightthickness=0, padx=0, pady=0, cursor='hand2', activeforeground=theme()['hover'], activebackground=theme()['bg']).pack()
tkinter.Button(win, text='Close', command=vpn.close, font=(font_type(), 20), fg=theme()['critical'], bg=theme()['bg'], relief='flat', overrelief='flat', borderwidth=0, highlightthickness=0, padx=0, pady=0, cursor='hand2', activeforeground=theme()['hover'], activebackground=theme()['bg']).pack()
separator(1)
tkinter.Button(win, text='☀️ Light Theme' if open(THEME_FILE).read() == 'light' else '🌑 Dark Theme', command=theme_toggle, font=(font_type(), 20), fg=theme()['fg'], bg=theme()['bg'], relief='flat', borderwidth=0, highlightthickness=0, padx=0, pady=0, cursor='hand2', activeforeground=theme()['hover'], activebackground=theme()['bg']).pack()

if vpn_name() != 'Lix':
    separator(2)
    tkinter.Button(win, text='LixVPN', command=open_info, font=(font_type(), 10, 'italic'), fg=theme()['fg'], bg=theme()['bg'], relief='flat', borderwidth=0, highlightthickness=0, padx=0, pady=0, cursor='hand2', activeforeground=theme()['hover'], activebackground=theme()['bg']).pack()

vpn.start()

win = win.mainloop()
