# -*- coding: utf-8 -*-

"""
DecoraterBotCore
~~~~~~~~~~~~~~~~~~~

Core to DecoraterBot

:copyright: (c) 2015 Decorater
:license: MIT, see LICENSE for more details.

"""

__title__ = 'DecoraterBotCore'
__author__ = 'Decorater'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015 Decorater'
__version__ = '1.0.0.12'
__build__ = 0x100000c

from .Core import changeWindowTitle, commands
import logging

try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
