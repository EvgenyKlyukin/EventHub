from .base import *

env = os.getenv('DJANGO_ENV', 'development')

if env == 'production':
    from .production import *
# elif env == 'test':
#     from .tests import *
else:
    from .development import *
