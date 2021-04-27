#!/usr/bin/env python
"""
Command to create a test super user. 
"""
if __name__ == "__main__":

    import pathlib
    import invoke
    import os
    import sys

    if len(sys.argv) != 3:
        print("Usage: createtestsuperuser.py <email> <password>")
        exit(1)

    ctx = invoke.context.Context()
    ctx.cd(pathlib.Path(__file__).parent.parent.as_posix())

    runner = invoke.runners.Local(ctx)
    runner.run('./manage.py createsuperuser', pty=True, watchers=[
        invoke.watchers.Responder('Email address:', sys.argv[1] + '\n'),
        invoke.watchers.Responder('Password', sys.argv[2]+ '\n'),
        invoke.watchers.Responder('Bypass password validation and create user anyway?', 'y\n'),
    ], timeout=5)
