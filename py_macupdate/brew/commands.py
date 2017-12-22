#!/usr/bin/env python3.6

import click


@click.command('update')
def update():
    """Update brew commands"""
    click.secho("Not implemented yet", fg='red')


@click.command('update_casks')
def update_casks():
    """Update brew casks commands"""
    click.secho("Not implemented yet", fg='red')
