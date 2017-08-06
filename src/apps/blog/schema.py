# coding: utf-8

#         app: org.toledano.blog
#      módulo: apps.blog.schema
# descripción: Esquemas de GraphQL para el blog
#       autor: Javier Sanchez Toledano
#       fecha: sábado, 5 de agosto de 2017

from graphene import relay, AbstractType       # , ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from apps.blog.models import Entry
from apps.blog.models import Category


# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['title', 'ingredients']
        interfaces = (relay.Node, )


class EntryNode(DjangoObjectType):
    class Meta:
        model = Entry
        filter_fields = {
            'title': ['exact', 'icontains', 'istartwith'],
            'body': ['icontains', ],
            'category': ['exact'],
            'category__name': ['exact']
        }
        interfaces = (relay.Node, )


class Query(AbstractType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    entry = relay.Node.Field(EntryNode)
    all_entries = DjangoFilterConnectionField(EntryNode)
