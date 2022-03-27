from django.shortcuts import render
from rest_framework import viewsets

from .serializers import BeachSerializer
from .models import Beach
# Create your views here.

class BeachViewSet(viewsets.ModelViewSet):
    queryset = Beach.objects.all()
    serializer_class = BeachSerializer