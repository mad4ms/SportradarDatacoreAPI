"""Compatibility shim for the vendored DataCore client.

This package exposes the vendored client located under the internal _vendor
namespace so external imports like ``datacore_client.api`` continue to work.
"""

from __future__ import annotations

from importlib import import_module
from importlib import util as importlib_util
from pkgutil import extend_path
from typing import TYPE_CHECKING

_spec = importlib_util.find_spec("_vendor.datacore_client")
if _spec is None or not _spec.submodule_search_locations:
    raise ModuleNotFoundError(
        "datacore_client is bundled inside sportradar_datacore_api under _vendor"
    )

__path__ = extend_path(__path__, __name__)
for _location in _spec.submodule_search_locations:
    if _location not in __path__:
        __path__.append(_location)

_vendor = import_module("_vendor.datacore_client")
__all__ = getattr(_vendor, "__all__", ())  # noqa: PLE0605
for _name in __all__:
    globals()[_name] = getattr(_vendor, _name)

if TYPE_CHECKING:
    from _vendor.datacore_client import AuthenticatedClient, Client  # noqa: F401
