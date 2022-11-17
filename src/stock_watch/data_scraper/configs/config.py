import logging
import os
import shutil
from sys import platform


class Config(object):
    """
    Config class
    """
    def __init__(self):
        # Handle reddit praw.ini file
        # Get current working directory
        self._working_dir = os.path.dirname(os.path.realpath(__file__))

    def copy_praw_ini_file_to_platform(self):
        # TODO: implement operation for Windows and MacOS
        if platform == "linux":
            try:
                praw_file_dir = os.path.join(self._working_dir, "praw.ini")
                home_dir = os.getenv("HOME") + "/.config" + "/praw.ini"
                shutil.copyfile(praw_file_dir, home_dir)
            except Exception as e:
                logging.error(e)
