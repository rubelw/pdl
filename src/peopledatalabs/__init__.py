__version__ = "0.1.0"

from .pdl import *
from peopledatalabs._version import __version__

# Append build number to version, if present (on build server)
try:
    from peopledatalabs._build import __build__
except ImportError:
    pass
else:
    __version__ = '{}.{}'.format(__version__, __build__)


