# -*- coding: UTF-8 -*-

#         app: org.toledano.blog
#      módulo: context
# descripción: Context Processor para el blog
#       autor: Javier Sanchez Toledano
#       fecha: domingo, 23 de agosto de 2015
from apps.blog.models import Category
__author__ = 'toledano'


def variables(request):
    TEMAS = Category.objects.all()

    AUTHOR = u'Javier Sanchez Toledano'
    SITENAME = u'Yo, Toledano'
    SITEURL = 'http://yo.toledano.org'
    STATICURL = 'https://media.toledano.org'
    SITELOGO = 'https://media.toledano.org/images/toledano-4.png'
    TAGLINE = u'Oh tiempo tus piramides'
    DEFAULT_METADATA = {
        'about_author': '''Soy programador en Django+Python y WordPress.
            Auditor líder certificado en la norma ISO 9001:2008.
            Fotógrafo aficionado.''',
        'email': 'js.toledano@me.com',
        'author': 'Javier Sanchez Toledano'
    }
    DISQUS_SITENAME = 'toledano'
    PROFILE_IMAGE_URL = 'https://media.toledano.org/images/yo.jpg'
    COVER_IMG = 'https://media.koding.mx/blog/assets/category_add.jpg'
    ARTICLE_COVER = 'https://media.toledano.org/images/toledano-cover.jpg'
    DOMAIN = "yo.toledano.org"
    FEEDBURNER = "http://feeds.feedburner.com/toledano/rss"

    # OpenGraph
    USE_OPEN_GRAPH = True
    TWITTER_USERNAME = "jstoledano"
    SITE_LANG = "es_MX"
    SITE_LANG_ALTERNATE = "es"
    OPEN_GRAPH_FB_APP_ID = "112184015464389"

    # ################ CASPER
    AUTHOR_PIC_URL = PROFILE_IMAGE_URL
    AUTHOR_BIO = DEFAULT_METADATA['about_author']
    AUTHOR_LOCATION = 'Tlaxcala, México'
    VECINO_ANTERIOR = '//media.toledano.org/casper/img/anterior.jpg'
    VECINO_SIGUIENTE = '//media.toledano.org/casper/img/siguiente.jpg'
    # ./CASPER

    return {
        'AUTHOR': AUTHOR,
        'SITENAME': SITENAME,
        'SITEURL': SITEURL,
        'STATICURL': STATICURL,
        'SITELOGO': SITELOGO,
        'TAGLINE': TAGLINE,
        'DISQUS_SITENAME': DISQUS_SITENAME,
        'PROFILE_IMAGE_URL': PROFILE_IMAGE_URL,
        'COVER_IMG': COVER_IMG,
        'ARTICLE_COVER': ARTICLE_COVER,
        'DOMAIN': DOMAIN,
        'FEEDBURNER': FEEDBURNER,
        'DEFAULT_METADATA': DEFAULT_METADATA,

        # Metadata (partials/_metaheader.html)
        'PUBLISHER': '',
        'GOOGLE_SV': 'hiMLLh1Fgb1J0rpXE4fw3zc7rRzKzbsg0y3c-6gujw0',
        'ALEXA': '',
        'MY_WOT': '',
        'MSVALIDATE': '',
        'GOOGLE_ANALYTICS': 'UA-130534-3',

        # OpenGraph
        'USE_OPEN_GRAPH': USE_OPEN_GRAPH,
        'TWITTER_USERNAME': TWITTER_USERNAME,
        'SITE_LANG': SITE_LANG,
        'SITE_LANG_ALTERNATE': SITE_LANG_ALTERNATE,
        'OPEN_GRAPH_FB_APP_ID': OPEN_GRAPH_FB_APP_ID,

        'TEMAS': TEMAS,

        # Casper
        'AUTHOR_PIC_URL': AUTHOR_PIC_URL,
        'AUTHOR_BIO': AUTHOR_BIO,
        'AUTHOR_LOCATION': AUTHOR_LOCATION,
        'VECINO_ANTERIOR': VECINO_ANTERIOR,
        'VECINO_SIGUIENTE': VECINO_SIGUIENTE
    }
