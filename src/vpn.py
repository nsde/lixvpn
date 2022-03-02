import os
import sys
import click
import colorama
import threading
import webbrowser
import subprocess
import tkinter.messagebox

colorama.init(autoreset=True)

@click.group()
def cli():
    pass

def run(command: str, *args, **kwargs):
    return subprocess.run(command, shell=True) or True

def run_threaded(command: str, threaded=False):
    try:
        print(command)
        thread = threading.Thread(target=run, args=([command])).start()
        return thread
    except Exception as e:
        tkinter.messagebox.showerror(title='Error!', message=e)
        return False

def shop():
    webbrowser.open('https://github.com/nsde/')

def vpns():
    return [f for f in os.listdir('vpns') if f.endswith('.ovpn')]

def prompt_sudo():
    ret = 0
    if os.geteuid() != 0:
        msg = '[LixVPN] sudo-password for %u:'
        ret = run(f'sudo -v -p "{}"')
    return ret

def start():
    if not ('--no-sudo' in sys.argv or '--ns' in sys.argv):
        prompt_sudo()

def close():
    run('pkill -f "gui.py"')
    run('sudo killall openvpn')
    run('pkill -f "cli.py"')

def connect(to: str):
    run(f'sudo openvpn --config vpns/{to} > connection.log')

@cli.command()
@click.option('-n', '--name', type=str, help='VPN Connection', default='lix')
def connect_cli(name: 'lix'):
    name = list(name)

    run(f'sudo openvpn --config vpns/{"".join(name)}.ovpn > connection.log')
    click.echo(colorama.Fore.BLUE + 'Connected with', name)

if __name__ == '__main__':
    print(colorama.Fore.BLUE + 'LixVPN started.')