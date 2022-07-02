from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from Link.models import Link
from Link.serializers import LinkSerializer


class PostListApi(viewsets.ModelViewSet):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateApi(viewsets.ModelViewSet):
    queryset = Link.objects.filter(active= True)
    serializer_class = LinkSerializer

class PostUpdateApi(viewsets.ModelViewSet):
    queryset = Link.objects.filter(active= True)
    serializer_class = LinkSerializer

class PostDeleteApi(viewsets.ModelViewSet):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializer


# Create your views here.
