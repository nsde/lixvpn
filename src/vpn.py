import os
import subprocess
import tkinter.messagebox

def run(command: str):
    try:
        return subprocess.run(command.split()) or True
    except Exception as e:
        tkinter.messagebox.showerror(title='Error!', message=e)
        return False

def prompt_sudo():
    ret = 0
    if os.geteuid() != 0:
        msg = "[LixVPN] sudo-password for %u:"
        ret = subprocess.check_call("sudo -v -p '%s'" % msg, shell=True)
    return ret

def start():
    prompt_sudo()

def setup():
    os.chdir(os.path.expanduser('/'))

def connect():
    run('sudo openvpn --config ~/lix.ovpn')