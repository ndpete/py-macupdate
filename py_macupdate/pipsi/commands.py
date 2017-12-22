#!/usr/bin/env python3.6
import click
import os
import subprocess


@click.command('update')
@click.option('--pkg', type=click.STRING, help='Update single package')
def pipsi_update(pkg):
    """Update pipsi command environments"""
    commands = []
    if pkg:
        cmd = ['pipsi', 'upgrade', pkg]
        commands.append(cmd)
    else:
        packages = get_installed()
        if packages:
            for pkg in packages:
                cmd = ['pipsi', 'upgrade', pkg]
                commands.append(cmd)

    for cmd in commands:
        click.secho(f'Upgrading: {cmd[2]}', fg='blue')
        run_cmd(cmd)


@click.command('upgrade-py')
@click.option('--pkg', type=click.STRING, help='Update single package')
@click.option('-f', '--force', is_flag=True, help="Supress Confirmation")
def pipsi_upgrade(pkg, force):
    """Upgrade Python Env for pipsi commands"""
    if not force:
        click.confirm("Warning, this will uninstall and reinstall pipsi installed scripts, Continue",
                      default=True, show_default=True, abort=True)
    commands = []
    if pkg:
        rmcmd = ['pipsi', 'uninstall', '--yes', pkg]
        newcmd = ['pipsi', 'install', pkg]
        commands.append(rmcmd)
        commands.append(newcmd)
    else:
        packages = get_installed()
        if packages:
            for pkg in packages:
                rmcmd = ['pipsi', 'uninstall', '--yes', pkg]
                newcmd = ['pipsi', 'install', pkg]
                commands.append(rmcmd)
                commands.append(newcmd)

    for cmd in commands:
        if cmd[2] == '--yes':
            click.secho(f'Upgrading: {cmd[3]}', fg='blue')
        run_cmd(cmd)


def get_installed():
    path = os.path.join(os.path.expanduser('~'), '.local', 'venvs')

    folders = []
    if os.path.isdir(path):
        folders = [f for f in os.listdir(
            path) if os.path.isdir(os.path.join(path, f))]
    return folders


def run_cmd(cmd: list):
    return subprocess.run(cmd)
