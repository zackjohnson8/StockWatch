import logging
import os
import shutil
import configparser
from sys import platform


class Config(object):
    def __init__(self):
        """
        Config class
        """
        self._working_dir = os.path.dirname(os.path.realpath(__file__))
        self._praw_file_dir = os.path.join(self._working_dir, "praw.ini")

    def copy_praw_ini_file_to_platform_folder(self):
        """
        Copy praw.ini file to platform folder
        :return:
        """
        if platform == "linux":
            try:
                home_dir = os.getenv("HOME") + "/.config" + "/praw.ini"
                shutil.copyfile(self._praw_file_dir, home_dir)
            except Exception as e:
                logging.error(e)
        elif platform == "win32":
            try:
                home_dir = os.getenv("APPDATA") + "/praw.ini"
                shutil.copyfile(self._praw_file_dir, home_dir)
            except Exception as e:
                logging.error(e)
        else:
            logging.error(f"Unsupported platform {platform}")

    def validate_site_name(self, site_name) -> bool:
        config_parser = configparser.ConfigParser()
        config_parser.read(self._praw_file_dir)
        if site_name not in config_parser.sections():
            logging.error("Please add a site named stock_watch_bot to the praw.ini file")
            return False

        configs = config_parser[site_name]
        if not self.has_required_fields(configs):
            logging.error(f"Please add the required fields to the praw.ini file")
            return False

    def has_required_fields(self, configs):
        required_fields = ["client_id", "client_secret", "username", "password", "user_agent"]
        for field in required_fields:
            config_value = configs[field]
            if self.starts_with(config_value, "<"):
                return False
        return True

    def starts_with(self, value, start):
        return value[0] == start
