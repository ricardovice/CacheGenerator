"""
CacheGenerator for Django

This module is based on Jared Kuolt's StaticGenerator available at
http://superjared.com/projects/static-generator/ that generates
static files to speed up HTTP request handling since static files
are way faster to serve then Django dynamic responses.

What is even faster, is if the response doesn't have to be read
from disk, and that is where CacheGenerator comes in.
The middleware provided will write the Django responses into
cache so that your webserver can easily read and respond at even
faster speed.
"""

