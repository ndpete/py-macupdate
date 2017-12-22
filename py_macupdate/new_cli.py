#!/usr/bin/env python3.6

import click
import pipsi
# from .awsparams import ls_param, cp_param, mv_param, rm_param, new_param, set_param, __VERSION__
__VERSION__ = '0.0.1'


@click.group()
@click.version_option(version=__VERSION__)
def main():
    pass

main.add_group(pipsi.main)


if __name__ == '__main__':
    main()
