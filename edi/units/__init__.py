# Copyright 2017 John Reese
# Licensed under the MIT license

import os.path
import logging

from pathlib import Path
from importlib import import_module
from types import ModuleType
from typing import List

log = logging.getLogger(__name__)


def import_units(root: Path = None) -> List[ModuleType]:
    """Find and import units in this path."""
    modules: List[ModuleType] = []

    if root is None:
        root = Path(__file__)
    if not root.is_dir():
        root = Path(root.parent)  # appease mypy, Path.parents -> PurePath

    log.debug(f"Searching for units in {root}...")
    for path in root.glob("*.py"):
        name = path.stem
        if name.startswith("_"):
            continue
        log.debug(f"Loading unit {name}")
        module = import_module(f"edi.units.{name}")
        modules.append(module)
    return modules
