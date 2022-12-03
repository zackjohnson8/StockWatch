import logging
from typing import Optional, Type, Dict, Any, Union
import praw
from praw.util.token_manager import BaseTokenManager
from prawcore import Requestor

from ..configs import config


class RedditAPI(object):
    """
    Praw Reddit API Decorator. This class is used to build functionality on top of the praw API. Most of the
    functionality is built using a 1-to-1 mapping of the Praw Reddit API which can be found at
    https://praw.readthedocs.io/en/stable/code_overview/reddit_instance.html
    """

    def __init__(self,
                 site_name: Optional[str] = None,
                 *,
                 config_interpolation: Optional[str] = None,
                 requestor_class: Optional[Type[Requestor]] = None,
                 requestor_kwargs: Optional[Dict[str, Any]] = None,
                 token_manager: Optional[BaseTokenManager] = None,
                 **config_settings: Optional[Union[str, bool, int]],
                 ):
        """
        :param config: If provided, the praw.ini file will be copied to the environment location that praw expects.
            If not provided, the praw.ini file must be in the praw environment location.
        :param site_name: The name of a section in your ``praw.ini`` file from which to
            load settings from. This parameter, in tandem with an appropriately
            configured ``praw.ini``, file is useful if you wish to easily save
            credentials for different applications, or communicate with other servers
            running Reddit. If ``site_name`` is ``None``, then the site name will be
            looked for in the environment variable ``praw_site``. If it is not found
            there, the ``DEFAULT`` site will be used (default: ``None``).
        :param config_interpolation: Config parser interpolation type that will be
            passed to :class:`.Config` (default: ``None``).
        :param requestor_class: A class that will be used to create a requestor. If not
            set, use ``prawcore.Requestor`` (default: ``None``).
        :param requestor_kwargs: Dictionary with additional keyword arguments used to
            initialize the requestor (default: ``None``).
        :param token_manager: When provided, the passed instance, a subclass of
            :class:`.BaseTokenManager`, will manage tokens via two callback functions.
            This parameter must be provided in order to work with refresh tokens
            (default: ``None``).
        """
        self._config = config.Config()
        # Validate that the praw.ini has site_name and the required fields
        if site_name:
            if not self._config.validate_site_name(site_name):
                return

        self._config.copy_praw_ini_file_to_platform_folder()

        self._reddit_api = praw.Reddit(
            site_name=site_name,
            config_interpolation=config_interpolation,
            requestor_class=requestor_class,
            requestor_kwargs=requestor_kwargs,
            token_manager=token_manager,
            **config_settings,
        )

        self._user = self._reddit_api.user

    @property
    def user(self):
        return self._user
