import graphene

from graphene_django.types import DjangoObjectType

from . import models

class MessageType(DjangoObjectType):
    class Meta:
        