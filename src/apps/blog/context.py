# -*- coding: UTF-8 -*-

#         app: org.toledano.blog
#      módulo: context
# descripción: Context Processor para el blog
#       autor: Javier Sanchez Toledano
#       fecha: domingo, 23 de agosto de 2015
from apps.blog.models import Category
__author__ = 'toledano'


def variables(request):
    return {
        'TEMAS': Category.objects.all(),
        'base_template': 'blog/amp' if request.es_amp else 'blog',
        'es_amp': request.es_amp,
    }
