from typing import Optional, Type, Dict, Any, Union
from praw.util.token_manager import BaseTokenManager
from prawcore import Requestor
import praw


class RedditAPI(praw.Reddit):
    def __init__(self,
                 site_name: Optional[str] = None,
                 *,
                 custom_config,
                 config_interpolation: Optional[str] = None,
                 requestor_class: Optional[Type[Requestor]] = None,
                 requestor_kwargs: Optional[Dict[str, Any]] = None,
                 token_manager: Optional[BaseTokenManager] = None,
                 **config_settings: Optional[Union[str, bool, int]],
                 ):

        # Validate that the praw.ini has site_name and the required fields
        if site_name:
            if not custom_config.validate_site_name(site_name):
                return

        custom_config.copy_praw_ini_file_to_platform_folder()


        super().__init__(site_name=site_name,
                         config_interpolation=config_interpolation,
                         requestor_class=requestor_class,
                         requestor_kwargs=requestor_kwargs,
                         token_manager=token_manager,
                         **config_settings)

        # Validate that connection with Reddit API is successful
        try:
            self.user.me()
        except Exception:
            raise Exception("Unable to connect to Reddit API. Please check your praw.ini file for valid credentials.")
