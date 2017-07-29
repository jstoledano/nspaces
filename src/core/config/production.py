from .base import *    # noqa

DEBUG = env.bool('DJANGO_DEBUG', default=False)
MIDDLEWARE += [
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware'
]
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')
ROLLBAR = {
    'access_token': env('ROLLBAR_TOKEN'),
    'environment': 'production',
    'branch': 'master',
    'root': ROOT_DIR,
}