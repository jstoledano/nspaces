# -*- coding: UTF-8 -*-

#         app: org.toledano.blog
#      módulo: blog.views
# descripción: Vistas del blog
#       autor: Javier Sanchez Toledano
#       fecha: jueves, 18 de junio de 2015


# from django.contrib.sitemaps import Sitemap
# from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
# from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView, UpdateView

from apps.blog.models import Entry
from apps.blog.models import Category


class EntryList(ListView):
    model = Entry
    paginate_by = 5
    make_object_list = True
    context_object_name = 'articles'
    template_name = 'blog/index.html'
    paginate_orphans = 1

    def get_queryset(self):
        return Entry.objects.filter(status=Entry.LIVE_STATUS)\
            .order_by('-pub_date', '-id',)


class Archivo(TemplateView):
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


class CategoryDetail(ListView):
    model = Entry
    context_object_name = 'cat'
    allow_empty = True
    paginate_by = 5
    template_name = 'blog/category_detail.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cat = get_object_or_404(Category, slug=self.kwargs['slug'])

    def get_queryset(self):
        return Entry.objects.filter(
            category=self.cat, status=Entry.LIVE_STATUS).select_related()\
                .order_by('-pub_date', 'id')

    def get_context_data(self, **kwargs):
        ctx = super(CategoryDetail, self).get_context_data(**kwargs)
        ctx['cat'] = self.cat
        return ctx


class TagList(ListView):
    paginate_by = 5
    context_object_name = 'tag'
    template_name = 'blog/tag.html'

    def get_context_data(self, **kwargs):
        from taggit.models import Tag
        ctx = super(TagList, self).get_context_data(**kwargs)
        ctx['t'] = Tag.objects.get(slug=self.kwargs['slug'])
        return ctx

    def get_queryset(self):
        return Entry.objects.filter(tags__slug=self.kwargs['slug']).distinct()
