# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import logging

logger = logging.getLogger(__name__)


class Sample(object):

    def __init__(self):
        """ Initializes for the extension.

        :return:
        """
        logger.debug("Extension sample created.")

    def start(self, context):
        """ starts the service this extension provides.

        :param context: the context provided the agent.
        """
        logger.debug("Hello from extension sample.")

    def stop(self, content):
        """ Stop the extension and release resources.

        :param content:
        """
        logger.debug("Sample extension stopped.")


