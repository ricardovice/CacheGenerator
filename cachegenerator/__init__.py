"""
CacheGenerator for Django

This module is based on Jared Kuolt's StaticGenerator available at
http://superjared.com/projects/static-generator/ that generates
static files to speed up HTTP request handling since static files
are way faster to serve then Django dynamic responses.

On some particular situations, such as using more than one server,
you might not want to write on disk and need your solution to be
on a central accessible place.
You might also have be serving content generated based on a lot of
different models, being impossible to track of the key entries they
are in, in this case you need a cache expire time.

The middleware provided will write the Django responses into cache
so that your webserver can easily read and respond at fast speed.
"""

