import vpn

import os
import tkinter
import tkinter.messagebox

if not os.path.exists('theme.txt'):
    open('theme.txt', 'w').write('light')

def get_theme():
    if open('theme.txt').read() == 'dark':
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

def font_type():
    return 'Yu Gothic' if os.name == 'nt' else 'URW Gothic' 

def theme_toggle():
    if open('theme.txt').read() == 'light':
        open('theme.txt', 'w').write('dark')
    else:
        open('theme.txt', 'w').write('light')

    if tkinter.messagebox.askyesno(title='Theme Toggle', message='The changes will apply after restarting.\nExit program now? (You need to start the program again for yourself.'):
        exit()

def separator(space=5):
    tkinter.Label(win, text='\n'*space, font=(font_type(), 5), fg=get_theme()['bg'], bg=get_theme()['bg']).pack()

def connect():
    vpn.connect()

win = tkinter.Tk()
win.config(bg=get_theme()['bg'])
win.title('LixVPN')
win.geometry('500x550')

separator(1)

title_row = tkinter.Frame(win, width=900, relief='flat', bd=0, bg=get_theme()['bg'], background=get_theme()['bg'], borderwidth=0)
title_row.pack()

tkinter.Label(title_row, text='Lix', font=(font_type(), 25, 'bold'), fg=get_theme()['fg'], bg=get_theme()['bg']).pack(side='left')
tkinter.Label(title_row, text='VPN', font=(font_type(), 25, 'bold'), fg=get_theme()['light'], bg=get_theme()['bg']).pack(side='left')
separator(1)

for v in vpn.vpns():
    tkinter.Button(win, text=v.title().split('.')[0], command=lambda v=v: vpn.connect(v), font=(font_type(), 20), fg=get_theme()['fg'], bg=get_theme()['bg'], relief='flat', overrelief='flat', borderwidth=0, highlightthickness=0, padx=0, pady=0, cursor='hand2', activeforeground=get_theme()['hover'], activebackground=get_theme()['bg']).pack()

separator(1)
tkinter.Button(win, text='How to add a VPN', command=vpn.close, font=(font_type(), 20), fg=get_theme()['light'], bg=get_theme()['bg'], relief='flat', overrelief='flat', borderwidth=0, highlightthickness=0, padx=0, pady=0, cursor='hand2', activeforeground=get_theme()['hover'], activebackground=get_theme()['bg']).pack()
tkinter.Button(win, text='VPN Shop', command=vpn.close, font=(font_type(), 20), fg=get_theme()['light'], bg=get_theme()['bg'], relief='flat', overrelief='flat', borderwidth=0, highlightthickness=0, padx=0, pady=0, cursor='hand2', activeforeground=get_theme()['hover'], activebackground=get_theme()['bg']).pack()
separator(1)
tkinter.Button(win, text='☀️ Light Theme' if open('theme.txt').read() == 'light' else '🌑 Dark Theme', command=theme_toggle, font=(font_type(), 20), fg=get_theme()['fg'], bg=get_theme()['bg'], relief='flat', borderwidth=0, highlightthickness=0, padx=0, pady=0, cursor='hand2', activeforeground=get_theme()['hover'], activebackground=get_theme()['bg']).pack()

vpn.start()

win = win.mainloop()