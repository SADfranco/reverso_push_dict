import _common

import trio


def exc1_fn():
    try:
        raise ValueError
    except Exception as exc:
        return exc


def exc2_fn():
    try:
        raise KeyError
    except Exception as exc:
        return exc


# This should be printed nicely, because Trio overrode sys.excepthook
raise trio.MultiError([exc1_fn(), exc2_fn()])
