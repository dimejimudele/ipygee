# coding=utf-8

""" A set of tools for working with Google Earth Engine Python API in Jupyter
notebooks """

from ._version import __version__
from .map import Map
from .assets import AssetManager
from .tasks import TaskManager
from . import chart
from .eprint import Eprint

eprint = Eprint()
