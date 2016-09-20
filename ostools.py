"""
ostools.py
"""

import os
import stat

def isfile(path):
    """Like os.path.isfile, but raises an exception on error."""
    return bool(stat.S_ISREG(os.stat(path).st_mode))

def isdir(path):
    """Like os.path.isdir, but raises an exception on error."""
    return bool(stat.S_ISDIR(os.stat(path).st_mode))
