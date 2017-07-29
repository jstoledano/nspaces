from unipath import Path
import environ

ROOT_DIR = Path(__file__).ancestor(3)
APPS_DIR = ROOT_DIR.child('apps')
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')

SECRET_KEY = env('DJANGO_SECRET_KEY')
DEBUG = env.bool('DJANGO_DEBUG', default=False)
ADMINS = (
    ("""Javier Sanchez Toledano""", 'js.toledano@me.com'),
)
MANAGERS = ADMINS

# Aplicaciones
ADMIN_TOOLS = [
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard'
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps'
]
THIRD_PARTY_APPS = [
    'authtools',
    'taggit',
    'taggit_templatetags2',
]
LOCAL_APPS = [
    'apps.profiles.config.UsersConfig',
    'apps.blog.config.BlogConfig'
]

INSTALLED_APPS = ADMIN_TOOLS + DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'core.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [APPS_DIR.child('templates')],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'apps.blog.context.variables',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'admin_tools.template_loaders.Loader'
            ]
        },
    },
]
WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': env.db('DATABASE_URL'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'Mexico/General'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = APPS_DIR.child('assets')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    str(APPS_DIR.child('static')),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

MEDIA_ROOT = APPS_DIR.child('media')
MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'profiles.User'

ADMIN_TOOLS_MENU = 'apps.dashboard.menu.CustomMenu'
ADMIN_TOOLS_INDEX_DASHBOARD = 'apps.dashboard.panels.CustomIndexDashboard'
