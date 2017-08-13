# coding: utf-8

#         app: blog.toledano.yo
#      módulo: core.schema
# descripción: Esquema global
#       autor: Javier Sanchez Toledano
#       fecha: sábado, 5 de agosto de 2017


import graphene
import apps.blog.schema


class Query(apps.blog.schema.Query, graphene.ObjectType):
    pass

grafo = graphene.Schema(query=Query)
