# -*- coding: utf-8 -*-
import logging

from formasaurus.utils import get_domain
from scrapy.exceptions import IgnoreRequest

logger = logging.getLogger(__name__)


class OffsiteDownloaderMiddleware:
    """
    This middleware filters out requests if they are not to the same domain
    as specified in request.meta['domain'].
    """
    def process_request(self, request, spider):
        if 'domain' not in request.meta:
            return

        domain = request.meta['domain']
        if get_domain(request.url) != domain:
            logger.info("Dropped request {}: it doesn't belong to {}".format(
                request, domain
            ))
            raise IgnoreRequest()