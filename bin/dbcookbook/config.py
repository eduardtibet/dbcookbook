# -*- coding: UTF-8 -*-

import os, os.path

__author__ = "Thomas Schraitle"
__version__ = "0.5"
__docformat__ = "epytext"

import sys

# We use configparser in order to make interpolation much more easier
# Furthermore it is possible to use a INI config style
#
# Conventions:
#  - Sections are capitalized, e.g. "PATHS"
#  - Entrys are written in lower case
from configparser import ConfigParser, ExtendedInterpolation, NoOptionError

class MyConfigParser(ConfigParser):
    """MyConfigParser using extended interpolation."""
    _DEFAULT_INTERPOLATION = ExtendedInterpolation()

# Read the INI file
INIFILE=os.path.join(os.path.dirname(__file__), 'dbcookbook.ini')
config = MyConfigParser()

res = config.read(INIFILE)
if res is None:
    # Not sure why FileNotFoundError doesn't take keyword arguments
    _E=FileNotFoundError("Could not find INI file")
    _E.filename = INIFILE
    _E.errno=12
    raise _E


# Our main XML file:
# MAINBASEFILE="DocBook-Cookbook.xml"
# MAINFILE="en/xml/{main}".format(main=MAINBASEFILE)

# Where to write logfiles:
LOGFILE=os.path.splitext(os.path.basename(__package__))[0]
# This strange expression makes sure the logfile is *always* set
LOGFILE=config.get('DEFAULT', 'logfile', fallback=LOGFILE ) % LOGFILE

try:    
    MAINFILE=config.get('DEFAULT', 'mainfile')
except NoOptionError as error:
    sys.stderr.write("ERROR: {error}".format( **locals() ))

# EOF