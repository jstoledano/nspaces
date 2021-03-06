# -*- coding: UTF-8 -*-

#         app: org.toledano.blog
#      módulo: blog.views
# descripción: Vistas del blog
#       autor: Javier Sanchez Toledano
#       fecha: jueves, 18 de junio de 2015

from functools import wraps

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.contrib.sitemaps import Sitemap
from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.decorators import available_attrs
# from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.decorators.cache import cache_page

from constance import config

from apps.blog.models import Entry
from apps.blog.models import Category

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def header(name, value):
    # View decorator that sets a response header.
    #
    # Example:
    # @header('X-Powered-By', 'Django')
    # def view(request, ...):
    #     ....
    #
    # For class-based views use:
    # @method_decorator(header('X-Powered-By', 'Django'))
    # def get(self, request, ...)
    #     ...
    def decorator(func):
        @wraps(func, assigned=available_attrs(func))
        def inner(request, *args, **kwargs):
            response = func(request, *args, **kwargs)
            response[name] = value
            return response
        return inner
    return decorator


class CacheMixin(object):
    cache_timeout = CACHE_TTL

    def get_cache_timeout(self):
        return self.cache_timeout

    def dispatch(self, *args, **kwargs):
        return cache_page(self.get_cache_timeout())(super(CacheMixin, self).dispatch)(*args, **kwargs)


class EntryList(ListView, CacheMixin):
    cache_timeout = CACHE_TTL
    model = Entry
    paginate_by = 6
    make_object_list = True
    context_object_name = 'articles'
    paginate_orphans = 1

    def get_queryset(self):
        return Entry.objects.filter(status=Entry.LIVE_STATUS) \
            .order_by('-pub_date', '-id', )

    def get_template_names(self):
        return ['%s/index.html' % ('blog/amp' if self.request.es_amp else 'blog')]


class Archivo(TemplateView, CacheMixin):
    cache_timeout = CACHE_TTL

    def get_context_data(self, **kwargs):
        ctx = super(Archivo, self).get_context_data(**kwargs)
        ctx['cats'] = Category.objects.all()
        ctx['entries'] = Entry.objects.order_by(
            '-pub_date', '-id').filter(status=Entry.LIVE_STATUS)
        return ctx

    def get_template_names(self):
        return ['%s/archivo.html' % ('blog/amp' if self.request.es_amp else 'blog')]


class EntryDetail(DetailView, CacheMixin):
    cache_timeout = CACHE_TTL
    model = Entry
    context_object_name = 'article'

    def get_template_names(self):
        return ['%s/entry_detail.html' % ('blog/amp' if self.request.es_amp else 'blog')]


class CategoryList(ListView, CacheMixin):
    cache_timeout = CACHE_TTL
    model = Category
    paginate_by = 6
    make_object_list = True
    context_object_name = 'cats'

    def get_template_names(self):
        return ['%s/category_list.html' % ('blog/amp' if self.request.es_amp else 'blog')]


class CategoryDetail(ListView, CacheMixin):
    cache_timeout = CACHE_TTL
    model = Entry
    context_object_name = 'cat'
    allow_empty = True
    paginate_by = 6

    def __init__(self, **kwargs):
        self.cat = ''
        super().__init__(**kwargs)

    def get(self, *args, **kwargs):
        if 'slug' in self.kwargs:
            try:
                entry = Entry.objects.get(slug=self.kwargs['slug'])
                return redirect(entry)
            except ObjectDoesNotExist:
                pass
        return super(CategoryDetail, self).get(*args, **kwargs)

    def get_queryset(self):
        self.cat = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Entry.objects.filter(
            category=self.cat, status=Entry.LIVE_STATUS).select_related() \
            .order_by('-pub_date', 'id')

    def get_context_data(self, **kwargs):
        ctx = super(CategoryDetail, self).get_context_data(**kwargs)
        ctx['cat'] = self.cat
        return ctx

    def get_template_names(self):
        return ['%s/category_detail.html' % ('blog/amp' if self.request.es_amp else 'blog')]


class TagCloud(TemplateView, CacheMixin):
    cache_timeout = CACHE_TTL
    template_name = 'blog/tag_cloud.html'


class TagList(ListView, CacheMixin):
    cache_timeout = CACHE_TTL
    paginate_by = 5
    context_object_name = 'tag'
    template_name = 'blog/tag.html'

    def get_context_data(self, **kwargs):
        from taggit.models import Tag
        ctx = super(TagList, self).get_context_data(**kwargs)
        ctx['t'] = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return ctx

    def get_queryset(self):
        return Entry.objects.filter(tags__slug=self.kwargs['slug']).distinct()


class BlogFeed(Feed, CacheMixin):
    """RSS de los artículos recientes"""
    # Debería usar las constantes en ./context.py para evitar repeticiones DRY
    title = config.SITENAME
    link = config.SITEURL
    description = config.RSS_DESCRIPTION
    site = config.SITEURL
    cache_timeout = CACHE_TTL

    item_author_name = config.AUTHOR
    item_author_email = config.AUTHOR_EMAIL
    item_author_link = config.SITEURL

    def items(self):
        return Entry.objects.filter(status=Entry.LIVE_STATUS).order_by('-pub_date')[:10]

    def item_pubdate(self, item):
        return item.pub_date

    def item_description(self, entry):
        return entry.resumen()


class BlogSitemap(Sitemap, CacheMixin):
    cache_timeout = CACHE_TTL
    changefreq = "never"
    priority = 0.5
    protocol = 'https'

    def items(self):
        return Entry.objects.filter(status=Entry.LIVE_STATUS)

    def lastmod(self, entry):   # pylint: disable=R0201
        return entry.pub_date

    def location(self, entry):
        return entry.get_absolute_url()


def error404(request):
    return render(request, 'blog/404.html')


def error500(request):
    return render(request, 'blog/500.html')
