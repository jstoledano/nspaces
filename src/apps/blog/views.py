# -*- coding: UTF-8 -*-

#         app: org.toledano.blog
#      módulo: blog.views
# descripción: Vistas del blog
#       autor: Javier Sanchez Toledano
#       fecha: jueves, 18 de junio de 2015

from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.contrib.sitemaps import Sitemap
from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.decorators.cache import cache_page

from apps.blog.models import Entry
from apps.blog.models import Category

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class CacheMixin(object):
    cache_timeout = 60

    def get_cache_timeout(self):
        return self.cache_timeout

    def dispatch(self, *args, **kwargs):
        return cache_page(self.get_cache_timeout())(super(CacheMixin, self).dispatch)(*args, **kwargs)


class EntryList(ListView, CacheMixin):
    cache_timeout = CACHE_TTL
    model = Entry
    paginate_by = 5
    make_object_list = True
    context_object_name = 'articles'
    template_name = 'blog/index.html'
    paginate_orphans = 1

    def get_queryset(self):
        return Entry.objects.filter(status=Entry.LIVE_STATUS) \
            .order_by('-pub_date', '-id', )


class Archivo(TemplateView, CacheMixin):
    cache_timeout = CACHE_TTL
    template_name = 'blog/archivo.html'

    def get_context_data(self, **kwargs):
        ctx = super(Archivo, self).get_context_data(**kwargs)
        ctx['cats'] = Category.objects.all()
        ctx['entries'] = Entry.objects.order_by(
            '-pub_date', '-id').filter(status=Entry.LIVE_STATUS)
        return ctx


class EntryDetail(DetailView):
    model = Entry
    context_object_name = 'article'
    template_name = 'blog/entry_detail.html'


class CategoryList(ListView, CacheMixin):
    cache_timeout = CACHE_TTL
    model = Category
    paginate_by = 5
    make_object_list = True
    context_object_name = 'cats'


class CategoryDetail(ListView):
    model = Entry
    context_object_name = 'cat'
    allow_empty = True
    paginate_by = 5
    template_name = 'blog/category_detail.html'

    def __init__(self, **kwargs):
        self.cat = ''
        super().__init__(**kwargs)

    def get_queryset(self):
        self.cat = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Entry.objects.filter(
            category=self.cat, status=Entry.LIVE_STATUS).select_related() \
            .order_by('-pub_date', 'id')

    def get_context_data(self, **kwargs):
        ctx = super(CategoryDetail, self).get_context_data(**kwargs)
        ctx['cat'] = self.cat
        return ctx


class TagCloud(TemplateView):
    template_name = 'blog/tag_cloud.html'


class TagList(ListView):
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
    title = 'Yo, Toledano'
    link = 'http://yo.toledano.org'  # URI of site
    description = 'Artículos recientes en Yo, Toledano'
    site = 'http://yo.toledano.org'
    cache_timeout = CACHE_TTL

    item_author_name = 'Javier Sanchez Toledano'
    item_author_email = 'yo@toledano.org'
    item_author_link = 'http://yo.toledano.org'  # URI of author

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
    protocol = 'http'

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
