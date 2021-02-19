from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import TraineesSerializer
from .models import Trainees


class TraineesView(viewsets.ModelViewSet):
    serializer_class = TraineesSerializer
    queryset = Trainees.objects.all()


def index(request):
    return HttpResponse('Hell there...')