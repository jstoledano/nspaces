# -*- coding: UTF-8 -*-

#         app: org.toledano.blog
#      módulo: blog.url
# descripción: Patrones de búsqueda del blog
#       autor: Javier Sanchez Toledano
#       fecha: sábado, 20 de junio de 2015

# from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.contrib import admin
# from django.contrib.sitemaps.views import sitemap
# from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
# from .views import (CategoriaCrear, CategoriaListar,
#                     EntradaDetail, EntradaCrear, EntryUpdate, EntryList,
#                     CategoriaEdit, TagList, TagCloud, Archivo, BlogFeed,
#                     BlogSitemap)
from apps.blog.views import EntryList
from apps.blog.views import EntryDetail
from apps.blog.views import CategoryDetail
from apps.blog.views import TagList
from apps.blog.views import Archivo

admin.autodiscover()
# sitemaps = {"blog": BlogSitemap}

urlpatterns = [
    url(r'^$', EntryList.as_view(), name='index'),
    url(r'^archivo/$', Archivo.as_view(), name='archivo'),

    url(r'^buscar/$',
        TemplateView.as_view(template_name='blog/buscar.html'),
        name='buscar'),

    url(r'^(?P<slug>[-\w]+)/$', CategoryDetail.as_view(), name="cat_detail"),
    url(r'^(?P<cat>[-\w]+)/(?P<slug>[-\w]+)/$',
        EntryDetail.as_view(), name="entry_detail"),
    url(r'^tag/(?P<slug>[-\w]+)/$', TagList.as_view(), name='tag_list'),
]

# urlpatterns = [
#     url(r'^$', EntryList.as_view(), name='index'),
#     url(r'^accounts/login/$',
#         auth_views.login,
#         {'template_name': 'admin/login.html'}),
#     url(r'^accounts/logout/$', auth_views.logout),
#     url(r'^archivo/$', Archivo.as_view(), name='archivo'),
#     url(r'^buscar/$',
#         TemplateView.as_view(template_name='blog/buscar.html'),
#         name='buscar'),
#     url(r'^entry/add/$',
#         login_required(EntradaCrear.as_view()), name="entry_add"),
#     url(r'^entry/(?P<pk>\d+)/edit/$',
#         login_required(EntryUpdate.as_view()), name="entry_edit"),
#     url(r'^cat/$', CategoriaListar.as_view(), name='cat_list'),
#     url(r'^cat/add/$',
#         login_required(CategoriaCrear.as_view()), name='cat_add'),
#     url(r'^cat/(?P<pk>\d+)/edit/$',
#         login_required(CategoriaEdit.as_view()), name='cat_edit'),
#     url(r'^tag/$', TagCloud.as_view(), name='tag_cloud'),
#     url(r'^tag/(?P<slug>[-\w]+)/$', TagList.as_view(), name='tag_list'),
#     url(r'^rss/$', BlogFeed()),
#     url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),
#     url(r'^(?P<slug>[-\w]+)/$', CategoriaDetalle.as_view(), name="cat_detail"),
#     url(r'^(?P<cat>[-\w]+)/(?P<slug>[-\w]+)/$',
#         EntradaDetail.as_view(), name="entry_detail"),
# ]
