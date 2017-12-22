#!/usr/bin/env python3.6

import click
import subprocess


@click.command('update')
def update():
    """Update brew commands"""
    click.secho("Checking for brew updates", fg='blue')
    subprocess.run(['brew', 'update'], stdout=subprocess.DEVNULL)
    outdated = subprocess.check_output(['brew', 'outdated'])
    if not outdated:
        click.secho("Brew is up-to-date", fg='green')
        return
    click.secho("Updating brew packages")
    subprocess.run(['brew', 'upgrade', '--cleanup'])


@click.command('outdated')
def outdated():
    """show outdated brew commands"""
    click.secho("Updating Brew references")
    subprocess.run(['brew', 'update'], stdout=subprocess.DEVNULL)
    subprocess.run(['brew', 'outdated'])


@click.command('update_casks')
def update_casks():
    """Update brew casks commands"""
    click.secho("Checking for cask updates", fg='blue')
    # subprocess.run(['brew', 'update'], stdout=subprocess.DEVNULL)
    outdated = subprocess.check_output(['brew', 'cask', 'outdated', "--quiet"])
    if not outdated:
        click.secho("Casks are up-to-date", fg='green')
        return
    outdated = outdated.decode('utf-8').strip().split('\n')
    raw_cmd = f'brew cask reinstall {" ".join(outdated)}'
    subprocess.run(raw_cmd.split(" "))
