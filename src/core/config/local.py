from .base import *    # noqa

DEBUG = env.bool('DJANGO_DEBUG', default=True)
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

MIDDLEWARE += [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware'
]
INSTALLED_APPS += (
    # 'debug_toolbar',
    'constance.backends.database',
)

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

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
CACHE_TTL = 1
