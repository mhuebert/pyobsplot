# Get __version__ from pyproject.toml (currently installed)
try:
    from importlib.metadata import PackageNotFoundError, version
except ImportError:
    from importlib_metadata import PackageNotFoundError, version  # type: ignore

try:
    __version__ = version("anywidget")
except PackageNotFoundError:
    __version__ = "uninstalled"


from .widget import Obsplot  # noqa:F401
from .parsing import Plot, d3, Math, js  # noqa:F401

__all__ = ["Obsplot", "Plot", "d3", "Math", "js", "__version__"]
