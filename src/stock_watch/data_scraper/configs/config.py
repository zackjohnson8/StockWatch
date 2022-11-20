import logging
import os
import shutil
from sys import platform


class Config(object):
    def __init__(self):
        """
        Config class
        """
        self._working_dir = os.path.dirname(os.path.realpath(__file__))

    def copy_praw_ini_file_to_platform_folder(self):
        """
        Copy praw.ini file to platform folder
        :return:
        """
        if platform == "linux":
            try:
                praw_file_dir = os.path.join(self._working_dir, "praw.ini")
                home_dir = os.getenv("HOME") + "/.config" + "/praw.ini"
                shutil.copyfile(praw_file_dir, home_dir)
            except Exception as e:
                logging.error(e)
        else:
            logging.error(f"Unsupported platform {platform}")
