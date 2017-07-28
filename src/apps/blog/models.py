# -*- coding: UTF-8 -*-

#         app: org.toledano.blog
#      módulo: blog.models
# descripción: Modelos usados en el blog
#       autor: Javier Sanchez Toledano
#       fecha: jueves, 27 de julio de 2017

import datetime
import uuid

from django.conf import settings
from django.core.urlresolvers import reverse
from django.template.defaultfilters import truncatechars_html, striptags
from django.db import models

import markdown
from taggit.managers import TaggableManager


MD_EXT = [
    'codehilite', 'meta', 'abbr', 'attr_list', 'def_list',
    'fenced_code', 'footnotes', 'smart_strong', 'tables',
    'headerid', 'sane_lists', 'extra', 'smarty', 'toc', 'admonition'
]

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.admonition': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.smarty': {},
        'markdown.extensions.toc': {},
        'markdown.extensions.sane_lists': {}
    }
}


class Trazabilidad(models.Model):
    """
    Una clase abstracta que sirve de base para modelos.
    Actualiza automáticamente los campos ``creado`` y ``modificado``.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(Trazabilidad):
    title = models.CharField(
        'Título', max_length=250, help_text="Máximo 250 caracteres"
    )
    slug = models.SlugField(
        unique=True, max_length=60,
        help_text="Se sugiere el texto generado por el título. Debe ser único."
    )
    description = models.TextField('Descripción')

    class Meta:
        ordering = ['slug']
        verbose_name_plural = "Categorías"
        verbose_name = 'Categoría'

    def __str__(self):
        return self.title

    def permalink(self):
        return '/cat/%s/' % self.slug

    def ruta(self):
        return '/%s/' % self.slug

    def get_absolute_url(self):
        return reverse('cat_detail', kwargs={'slug': self.slug})
