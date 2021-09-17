#!/usr/bin/env python3
import json
import base64
from typing import Tuple, List

import click


def replace_color(msg: str) -> str:
    replacements = ["&0/\033[0;30m", "&1/\033[0;34m", "&2/\033[0;32m", "&3/\033[0;36m", "&4/\033[0;31m", "&5/\033[0;35m", "&6/\033[0;33m", "&7/\033[0;37m", "&8/\033[1;30m", "&9/\033[1;34m", "&a/\033[1;32m", "&b/\033[1;36m", "&c/\033[1;31m", "&d/\033[1;35m", "&e/\033[1;33m", "&f/\033[1;37m", "&r/\033[0m", "&n/\n"]
    for r in replacements:
        msg = msg.replace(r[:2], r[3:])
    return msg


@click.group()
@click.argument('var')
@click.pass_context
def cli(ctx, var: str):
    # Get saved parts
    parts: List[Tuple[int, str]] = json.loads(base64.b64decode(var.encode()).decode()) if var != '' else []
    ctx.obj['parts'] = parts
    pass


@cli.command()
@click.pass_context
@click.option('--color', default=True)
def show(ctx, color: bool):
    parts = ctx.obj['parts']
    parts.sort(key=lambda p: p[0])
    s = ''.join([p[1] for p in parts])
    if color:
        s = replace_color(s)
    print(s)


@cli.command()
@click.pass_context
def debug(ctx):
    print(ctx.obj['parts'])


@cli.command()
@click.argument('order')
@click.argument('format')
@click.pass_context
def set(ctx, order: str, format: str):
    order = int(order)
    parts = ctx.obj['parts']

    # Create new parts list
    existing = [p for p in parts if p[0] == order]
    if existing:
        parts.remove(existing[0])
    parts.append((order, format))
    print(base64.b64encode(json.dumps(parts).encode()).decode())


if __name__ == '__main__':
    cli(obj={})
