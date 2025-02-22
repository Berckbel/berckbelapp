import re

def validate_url(url):
    patron = re.compile(
        r'^(https?://)?'
        r'([a-zA-Z0-9.-]+)'
        r'(\.[a-zA-Z]{2,6})'
        r'(:\d+)?'
        r'(/[\w.-]*)*'
        r'(\?.*)?'
        r'(#.*)?$'
    )
    return bool(patron.match(url))
