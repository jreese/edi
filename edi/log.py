# Copyright 2017 John Reese
# Licensed under the MIT license

import logging
import sys


def init_logger(
    stdout: bool = True, file_path: str = None, debug: bool = False
) -> logging.Logger:
    """Initialize the logging system for stdout and an optional log file."""

    log = logging.getLogger("")

    level = logging.DEBUG if debug else logging.INFO
    log.setLevel(level)

    logging.addLevelName(logging.ERROR, "E")
    logging.addLevelName(logging.WARNING, "W")
    logging.addLevelName(logging.INFO, "I")
    logging.addLevelName(logging.DEBUG, "V")

    date_fmt = r"%H:%M:%S"
    stdout_fmt = "%(levelname)s: %(message)s"
    verbose_fmt = (
        "%(asctime)s,%(msecs)d %(levelname)s "
        "%(module)s:%(funcName)s():%(lineno)d   "
        "%(message)s"
    )

    handler: logging.Handler

    if stdout:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)

        if debug:
            handler.setFormatter(logging.Formatter(verbose_fmt, date_fmt))
        else:
            handler.setFormatter(logging.Formatter(stdout_fmt, date_fmt))

        log.addHandler(handler)

    if file_path:
        handler = logging.FileHandler(file_path)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(logging.Formatter(verbose_fmt, date_fmt))

        log.addHandler(handler)

    return log
