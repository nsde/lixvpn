import os
import sys
import colorama
import threading
import webbrowser
import subprocess
import gh_md_to_html
import tkinter.messagebox

cwd = os.getcwd()
colorama.init(autoreset=True)

def run(command: str, *args, **kwargs):
    return subprocess.run(command, shell=True) or True

def run_threaded(command: str, threaded=False):
    try:
        print(colorama.Fore.MAGENTA + command)
        thread = threading.Thread(target=run, args=([command])).start()
        return thread
    except Exception as e:
        tkinter.messagebox.showerror(title='Error!', message=e)
        return False

def convert_and_show(doc: str):
    html_code = gh_md_to_html.main(f'{cwd}/docs/{doc}.md', website_root=cwd, enable_css_saving=False)
    html_path = f'{cwd}/docs/generated/{doc}.html'
    open(html_path, 'w').write(html_code)
    webbrowser.open(html_path)

def show_shop():
    convert_and_show('shop')

def show_tutorial():
    webbrowser.open(cwd + '/docs/shop.md')

def show_log():
    webbrowser.open()

def vpns():
    return [f for f in os.listdir('vpns') if f.endswith('.ovpn')]

def prompt_sudo():
    return
    ret = 0
    if os.geteuid() != 0:
        ret = run(f'sudo -v -p "[LixVPN] sudo-password for %u:"')
    return ret

def start():
    if not ('--no-sudo' in sys.argv or '--ns' in sys.argv):
        prompt_sudo()

    print(colorama.Fore.BLUE + 'LixVPN started.')

def close():
    run('pkill -f "gui.py"')
    run('sudo killall openvpn')
    run('pkill -f "cli.py"')

def connect(to: str):
    run(f'sudo openvpn --config vpns/{to} > logs/connection.log')
