#!/usr/bin/env python3.6

import click
import subprocess


@click.command('outdated')
def outdated():
    """list outdated apps"""
    subprocess.run(['mas', 'outdated'])


@click.command('update')
def update():
    """Update Mac App Store Apps"""
    subprocess.run(['mas', 'upgrade'])
