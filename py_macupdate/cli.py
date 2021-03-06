#!/usr/bin/env python3.6

import click
from pipsi import commands as pipsi_cmd
from brew import commands as brew_cmd
from system_cmd import commands as sys_cmd
from mas import commands as mas_cmd
# from .awsparams import ls_param, cp_param, mv_param, rm_param, new_param, set_param, __VERSION__
__VERSION__ = '0.0.1'

@click.group()
@click.version_option(version=__VERSION__)
def main():
    pass


@main.group()
def pipsi():
    """
    Manage Pipsi Updates
    """
    pass


pipsi.add_command(pipsi_cmd.update)
pipsi.add_command(pipsi_cmd.upgrade)
pipsi.add_command(pipsi_cmd.upgrade_py)


@main.group()
def brew():
    """
    Update brew installed apps
    """
    pass


brew.add_command(brew_cmd.update)
brew.add_command(brew_cmd.outdated)
brew.add_command(brew_cmd.update_casks)


@main.group()
def system():
    """
    Run system updates
    """
    pass


system.add_command(sys_cmd.update)


@main.group()
def mas():
    """
    Update Mac App Store Apps
    """
    pass


mas.add_command(mas_cmd.outdated)
mas.add_command(mas_cmd.update)


@main.command('upgrade_all')
@click.option('-f', '--force', is_flag=True, help="Supress Confirmation")
@click.pass_context
def upgrade_all(ctx, force):
    """
    Upgrade everything at once
    """
    if not force:
        force = click.confirm("Warning, this will upgrade all packages apps, and the os. It may or may not require a restart once finished. Continue",
                              default=True, show_default=True, abort=True)
    ctx.invoke(brew_cmd.update)
    ctx.invoke(brew_cmd.update_casks)
    ctx.invoke(pipsi_cmd.update)
    ctx.invoke(mas_cmd.update)
    ctx.invoke(sys_cmd.update, force=force)
    click.secho("Finished updateing all the things", fg='green')


if __name__ == '__main__':
    main()
