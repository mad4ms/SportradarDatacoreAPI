"""Initialization file for the sportradar_datacore_api package.

Author: Michael Adams, 2025
"""

from __future__ import annotations

import sys
from importlib import import_module
from importlib import util as importlib_util
from types import ModuleType

if importlib_util.find_spec("datacore_client") is None:
    _vendored: ModuleType | None
    try:
        _vendored = import_module("_vendor.datacore_client")
    except ModuleNotFoundError:
        _vendored = None
    else:
        sys.modules.setdefault("datacore_client", _vendored)
