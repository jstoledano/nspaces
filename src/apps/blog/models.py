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
    'markdown.extensions.codehilite',
    'markdown.extensions.meta',
    'markdown.extensions.abbr',
    'markdown.extensions.attr_list',
    'markdown.extensions.def_list',
    'markdown.extensions.fenced_code',
    'markdown.extensions.footnotes',
    'markdown.extensions.tables',
    'markdown.extensions.smart_strong',
    'markdown.extensions.admonition',
    'markdown.extensions.headerid',
    'markdown.extensions.sane_lists',
    'markdown.extensions.extra',
    'markdown.extensions.smarty',
    'markdown.extensions.toc',
]


class Trazabilidad(models.Model):
    """
    Una clase abstracta que sirve de base para modelos.
    Actualiza automáticamente los campos ``creado`` y ``modificado``.
    """
    idx = models.UUIDField(default=uuid.uuid4, editable=False)
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
    icon = models.CharField(max_length=20, blank=True)
    description = models.TextField('Descripción')
    description_html = models.TextField(editable=False, blank=True)

    class Meta:
        ordering = ['slug']
        verbose_name_plural = "Categorías"
        verbose_name = 'Categoría'

    def save(self, force_insert=False, force_update=False, **kwargs):
        self.description_html = markdown.markdown(
            self.description,
            output_format='html5',
            lazy_ol=True,
            extensions=MD_EXT
        )
        super(Category, self).save(force_insert, force_update)

    def __str__(self):
        return self.title

    def permalink(self):
        return '/cat/%s/' % self.slug

    def ruta(self):
        return '/%s/' % self.slug

    def get_absolute_url(self):
        return reverse('cat_detail', kwargs={'slug': self.slug})


class Entry(Trazabilidad):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )

    # Campos principales
    title = models.CharField('Título', max_length=250)
    summary = models.TextField('Resumen', blank=True)
    body = models.TextField('Contenido')
    extend = models.TextField('Extendido', blank=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    # Campos para generar el html generado con markdown
    summary_html = models.TextField(editable=False, blank=True)
    body_html = models.TextField(editable=False, blank=True)
    extend_html = models.TextField(editable=False, blank=True)

    # Metadata
    enable_comments = models.BooleanField(default=True)
    cover = models.URLField(blank=True)
    slug = models.SlugField(unique_for_date='pub_date')
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)
    featured = models.BooleanField(default=False)

    # Taxonomía
    category = models.ForeignKey(Category)
    tags = TaggableManager()

    # Seguimiento
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='entradas',
        editable=False
    )

    class Meta:
        verbose_name_plural = 'Entradas'
        verbose_name = 'Entrada'
        ordering = ['-id', '-pub_date']
        unique_together = ('slug', 'pub_date')
        get_latest_by = 'pub_date'

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, **kwargs):
        self.body_html = markdown.markdown(
            self.body,
            output_format='html5',
            lazy_ol=True,
            extensions=MD_EXT
        )
        if self.summary:
            self.summary_html = markdown.markdown(
                self.summary,
                output_format='html5',
                lazy_ol=True,
                extensions=MD_EXT
            )
        if self.extend:
            self.extend_html = markdown.markdown(
                self.extend,
                output_format='html5',
                lazy_ol=True,
                extensions=MD_EXT
            )
        super(Entry, self).save(force_insert, force_update)

    def resumen(self):
        if self.summary:
            return striptags(self.summary)
        else:
            return striptags(truncatechars_html(self.body_html, 250))

    def get_absolute_url(self):
        return reverse(
            'entry_detail',
            kwargs={'cat': self.category.slug, 'slug': self.slug}
        )

    def siguiente(self):
        try:
            return self.get_next_by_pub_date()
        except self.DoesNotExist:
            return None

    def anterior(self):
        try:
            return self.get_previous_by_pub_date()
        except self.DoesNotExist:
            return None
