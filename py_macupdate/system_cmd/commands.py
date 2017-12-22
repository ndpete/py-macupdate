#!/usr/bin/env python3.6

import click
import subprocess


@click.command('update')
@click.option('-f', '--force', is_flag=True, help="Supress Confirmation")
def update(force):
    """Run OS Updates"""
    if not force:
        click.confirm("Warning, this will install all system updates and may require a restart, Continue",
                      default=True, show_default=True, abort=True)
    cmd = "sudo -k softwareupdate -i -a"
    click.secho("Prompting for sudo password", fg='blue')
    subprocess.run(cmd.split(" "))
