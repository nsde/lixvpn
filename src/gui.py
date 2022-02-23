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
            'warn': '#fc9d19',
            'critical': '#fc3b19',
            'ok': '#28ff02'
        }
    else:
        return {
            'fg': 'black',
            'bg': 'white',
            'light': '#008AE6',
            'warn': '#fc9d19',
            'critical': '#fc3b19',
            'ok': '#28ff02'
        }        

def font_type():
    return 'Consolas' if os.name == 'nt' else 'FreeMono' 

def theme_toggle():
    if open('theme.txt').read() == 'light':
        open('theme.txt', 'w').write('dark')
    else:
        open('theme.txt', 'w').write('light')

    if tkinter.messagebox.askyesno(title='Theme Toggle', message='The changes will apply after restarting.\nExit program now? (You need to start the program again for yourself.'):
        exit()

win = tkinter.Tk() # neues Fenster
win.config(bg=get_theme()['bg'])
win.title('LixVPN') # Fenstertitel
win.geometry('500x550') # Größe des Fensters in Pixel

# label = Textfeld
title_label = tkinter.Label(win, text='LixVPN', font=(font_type(), 20), fg=get_theme()['fg'], bg=get_theme()['bg'])
title_label.pack()

display_label = tkinter.Label(win, text='', font=(font_type(), 40), fg=get_theme()['light'], bg=get_theme()['bg']) # Übersicht für das Ergebnis
display_label.pack()

tkinter.Button(win, text='☀️ Light Theme' if open('theme.txt').read() == 'light' else '🌑 Dark Theme', command=theme_toggle, font=(font_type(), 30, 'bold'), fg=get_theme()['fg'], bg=get_theme()['bg'], relief='flat').pack()
tkinter.Button(win, text='Setup', command=vpn.setup, font=(font_type(), 30, 'bold'), fg=get_theme()['light'], bg=get_theme()['bg'], relief='flat').pack()
tkinter.Button(win, text='Connect', command=vpn.connect, font=(font_type(), 30, 'bold'), fg=get_theme()['light'], bg=get_theme()['bg'], relief='flat').pack()

vpn.start()

win = win.mainloop() # diese Zeile muss IMMER ganz unten im Code sein, das startet das Fenster.