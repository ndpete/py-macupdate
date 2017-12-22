#!/usr/bin/env python3.6

import click


@click.command('update')
def pipsi_update():
    """Update pipsi command environments"""
    click.secho("Not implemented yet", fg='red')


@click.command('upgrade-py')
def pipsi_upgrade():
    """Upgrade Python Env for pipsi commands"""
    click.secho("Not implemented yet", fg='red')
