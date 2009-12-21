import re
from django.conf import settings
from django.core.cache import cache


class CacheGeneratorMiddleware(object):
    """
    This requires settings.CACHE_GENERATOR_URLS tuple to match on URLs
    
    Example::
        
        CACHE_GENERATOR_URLS = (
            (r'^/$', 300), # 5 minutes cache timeout for the root
            (r'^/blog', 600), #  10 minutes cache timeout for the blog
        )
        
    """
    urls = tuple([(re.compile(url[0]), url[1]) for url in settings.CACHE_GENERATOR_URLS])
    
    def process_response(self, request, response):
        if response.status_code == 200:
            for url in self.urls:
                if url[0].match(request.path):
                    cache.set(request.META['REQUEST_URI'], response.content, url[1])
                    break
        return response

