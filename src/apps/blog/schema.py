# coding: utf-8

#         app: org.toledano.blog
#      módulo: apps.blog.schema
# descripción: Esquemas de GraphQL para el blog
#       autor: Javier Sanchez Toledano
#       fecha: sábado, 5 de agosto de 2017

import graphene
from graphene import relay, AbstractType       # , ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
# from graphene_django.fields import DjangoConnectionField
from graphene_django.debug import DjangoDebug

from taggit.models import Tag
from apps.blog.models import Entry
from apps.blog.models import Category


class TagNode(DjangoObjectType):
    class Meta:
        model = Tag
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'slug': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['title', ]
        interfaces = (relay.Node, )


class EntryNode(DjangoObjectType):
    tags = graphene.List(source='get_tags', of_type=graphene.String)
    status = graphene.Int(source='get_status')
    autor = graphene.String(source='get_autor')
    # tags = DjangoConnectionField(TagNode)

    class Meta:
        model = Entry
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'body': ['icontains', ],
            'category': ['exact', ],
        }
        interfaces = (relay.Node, )


class Query(AbstractType):
    debug = graphene.Field(DjangoDebug, name='__debug')

    tag = relay.Node.Field(TagNode)
    all_tags = DjangoFilterConnectionField(TagNode)

    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    entry = relay.Node.Field(EntryNode)
    all_entries = DjangoFilterConnectionField(EntryNode)
