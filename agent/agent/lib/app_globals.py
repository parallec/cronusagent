#pylint: disable=W0105
"""The application's Globals object"""

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

import logging
LOG = logging.getLogger(__name__)

class Globals(object):
    """Globals acts as a container for objects available throughout the
    life of the application

    """

    def __init__(self, config):
        """One instance of Globals is created during application
        initialization and is available during requests via the
        'app_globals' variable

        """
        self.cache = CacheManager(**parse_cache_config_options(config))


