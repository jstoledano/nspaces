# -*- coding: UTF-8 -*-

#         app: org.toledano.blog
#      módulo: blog.url
# descripción: Patrones de búsqueda del blog
#       autor: Javier Sanchez Toledano
#       fecha: sábado, 20 de junio de 2015

from django.conf.urls import url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView

from apps.blog.views import EntryList
from apps.blog.views import EntryDetail
from apps.blog.views import CategoryList
from apps.blog.views import CategoryDetail
from apps.blog.views import TagCloud
from apps.blog.views import TagList
from apps.blog.views import Archivo
from apps.blog.views import BlogFeed
from apps.blog.views import BlogSitemap

admin.autodiscover()
sitemaps = {"blog": BlogSitemap}

urlpatterns = [
    # Portada
    url(r'^$', EntryList.as_view(), name='index'),

    # robots.txt y otros archivos de texto
    url(r'^robots\.txt$',
        TemplateView.as_view(template_name='blog/textos/robots.txt', content_type='text/plain'), name='robots'),
    url(r'^socialmedia\.txt$',
        TemplateView.as_view(template_name='blog/textos/socialmedia.txt', content_type='text/plain'),
        name='socialmedia'),
    url(r'^keybase\.txt$',
        TemplateView.as_view(template_name='blog/textos/keybase.txt', content_type='text/plain'), name='keybase'),

    # Páginas sin relación con modelos en apps.blog
    url(r'^archivo/$', Archivo.as_view(), name='archivo'),
    url(r'^buscar/$', TemplateView.as_view(template_name='blog/buscar.html'), name='buscar'),
    url(r'^rss/$', BlogFeed(), name='rss_feed'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),

    # URIs relacionadas con etiquetas
    url(r'^tag/$', TagCloud.as_view(), name='tag_cloud'),
    url(r'^tag/(?P<slug>[-\w]+)/$', TagList.as_view(), name='tag_list'),

    # Las categorías entran en conflicto con las etiquetas
    url(r'^cats/$', CategoryList.as_view(), name='cats'),
    url(r'^(?P<slug>[-\w]+)/$', CategoryDetail.as_view(), name="cat_detail"),

    # Esta es la última entrada porque captura todo
    url(r'^(?P<cat>[-\w]+)/(?P<slug>[-\w]+)/$', EntryDetail.as_view(), name="entry_detail"),
]
