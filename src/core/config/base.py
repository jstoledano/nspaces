from unipath import Path
import environ
from collections import OrderedDict

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
ADMIN_DASHBOARD = [
    'flat_responsive',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites'
]
THIRD_PARTY_APPS = [
    'authtools',
    'taggit',
    'taggit_templatetags2',
    'taggit_autosuggest',
    'constance',
    'corsheaders',
    'draceditor'
]
LOCAL_APPS = [
    'apps.profiles.config.UsersConfig',
    'apps.blog.config.BlogConfig'
]

INSTALLED_APPS = ADMIN_DASHBOARD + DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'apps.blog.middleware.AmpMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]
ROOT_URLCONF = 'core.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [APPS_DIR.child('templates')],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'constance.context_processors.config',
                'apps.blog.context.variables',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
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
LANGUAGE_CODE = 'es'
TIME_ZONE = 'Mexico/General'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = APPS_DIR.child('assets')
STATIC_URL = '/assets/'
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
SITE_ID = '1'

TAGGIT_TAGCLOUD_MIN = 1
TAGGIT_TAGCLOUD_MAX = 6
TAGGIT_LIMIT = 200

CORS_ORIGIN_REGEX_WHITELIST = (r'https?://(localhost|127\.0\.0\.1|.*\.toledano\.org)(:[0-9]+)?', )

DRACEDITOR_ENABLE_CONFIGS = {
    'imgur': 'true',
    'mention': 'false',
    'jquery': 'true',
}
DRACEDITOR_IMGUR_CLIENT_ID = env('DRACEDITOR_IMGUR_CLIENT_ID')
DRACEDITOR_IMGUR_API_KEY = env('DRACEDITOR_IMGUR_API_KEY')



CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True
CONSTANCE_CONFIG = {
    'SITENAME': ('Yo, Toledano', 'Nombre del sitio'),
    'TAGLINE': ('Oh tiempo tus piramides', 'Descripción del sitio'),
    'SITEURL': ('https://yo.toledano.org', 'Dirección web del sitio'),
    'RSS_DESCRIPTION': ('Artículos recientes en Yo, Toledano', 'Descripción para la fuente RSS'),
    'DOMAIN': ('yo.toledano.org', 'Dominio'),

    'LICENCE': ('https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es', 'Licencia del sitio'),
    'LICENCE_IMAGE': ('/assets/blog/img/80x15.png', 'Imagen de la licencia'),

    'AUTHOR': ('Javier Sanchez Toledano', 'Editor principal'),
    'AUTHOR_EMAIL': ('javier@toledano.org', 'Correo del editor principal'),

    'PUBLISHER': ('', 'AdSense Publisher ID'),
    'GOOGLE_SV': ('hiMLLh1Fgb1J0rpXE4fw3zc7rRzKzbsg0y3c-6gujw0', 'Google SV id'),
    'ALEXA': ('', 'Verificador de Alexa'),
    'MY_WOT': ('', 'Verificador de WOT'),
    'MSVALIDATE': ('', 'Verificador de Bing'),
    'GOOGLE_ANALYTICS': ('UA-130534-3', 'ID de Google Analytics'),

    'STATICURL': ('https://media.toledano.org', 'URL de los archivos estáticos'),
    'SITELOGO': ('https://media.toledano.org/images/toledano-4.png', 'Logo del sitio'),
    'COVER_IMG': ('/assets/blog/img/category_add_95d30aaa88ef6cdcb41daa7f39c02543.jpg', 'URL de la imagen de portada'),
    'ARTICLE_COVER': ('https://media.toledano.org/images/toledano-cover.jpg', 'URL de la imagen de los artículos'),
    'PROFILE_IMAGE_URL': ('https://media.toledano.org/images/yo.jpg', 'URL de la imagen de perfil'),

    'DISQUS_SITENAME': ('toledano', 'Identificación de Disqus'),
    'FEEDBURNER': ('http://feeds.feedburner.com/toledano/rss', 'URL de las fuentes RSS en Feedburner'),
    'TWITTER_USERNAME': ('jstoledano', 'Usuario de Twitter'),
    'USE_OPEN_GRAPH': (True, 'Se usará OpenGraph', bool),
    'SITE_LANG': ('es_MX', 'Idioma del sitio'),
    'SITE_LANG_ALTERNATE': ('es', 'Idioma alterno'),
    'OPEN_GRAPH_FB_APP_ID': ('112184015464389', 'Identificador de la App de Facebook'),

    'VECINO_ANTERIOR': ('https://media.toledano.org/casper/img/anterior.jpg', 'URL de la imagen del artículo anterior'),
    'VECINO_SIGUIENTE': (
        'https://media.toledano.org/casper/img/siguiente.jpg', 'URL de la imagen del artículo siguiente'
    )
}

CONSTANCE_CONFIG_FIELDSETS = OrderedDict([
    ('Sobre el sitio', (
        'SITENAME',
        'TAGLINE',
        'SITEURL',
        'RSS_DESCRIPTION',
        'DOMAIN')),
    ('Licencia', (
        'LICENCE',
        'LICENCE_IMAGE'
    )),
    ('Metadata', (
        'PUBLISHER',
        'GOOGLE_SV',
        'ALEXA',
        'MY_WOT',
        'MSVALIDATE',
        'GOOGLE_ANALYTICS'
    )),
    ('Editor Principal', (
        'AUTHOR',
        'AUTHOR_EMAIL'
    )),
    ('Temas e Imágenes', (
        'STATICURL',
        'SITELOGO',
        'COVER_IMG',
        'ARTICLE_COVER',
        'PROFILE_IMAGE_URL',
    )),
    ('Redes Sociales', (
        'DISQUS_SITENAME',
        'FEEDBURNER',
        'TWITTER_USERNAME',
        'USE_OPEN_GRAPH',
        'SITE_LANG',
        'SITE_LANG_ALTERNATE',
        'OPEN_GRAPH_FB_APP_ID'
    )),
    ('Paginación', (
        'VECINO_ANTERIOR',
        'VECINO_SIGUIENTE'
    )),
])
