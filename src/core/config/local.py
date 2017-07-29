from .base import *    # noqa

DEBUG = env.bool('DJANGO_DEBUG', default=True)

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware'
]
INSTALLED_APPS += ('debug_toolbar', )

INTERNAL_IPS = ['127.0.0.1', ]
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')

ROLLBAR = {
    'access_token': env('ROLLBAR_TOKEN'),
    'environment': 'development' if DEBUG else 'production',
    'branch': 'master',
    'root': ROOT_DIR,
}

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}
