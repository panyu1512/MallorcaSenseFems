from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import BeachSerializer, TrashSerializer
from .models import Beach, Trash   

# Create your views here.
class TrashViewSet(viewsets.ModelViewSet):
    queryset = Trash.objects.all()
    serializer_class = TrashSerializer

    @action(detail=True, methods=['GET'])    
    def contaminatedBeaches(self, request):
        beaches = Beach.objects.filter(num_residues__gt=0).order_by('num_residues').distinct()
        serializer = BeachSerializer(beaches, many=True)
        return Response(serializer.data)
    
    #funtion to get the last 20 pickups
    @action(detail=True, methods=['GET'])
    def lastPickUps(self, request):
        pickups = Trash.objects.order_by('-pickup_date').distinct()[:20]
        serializer = TrashSerializer(pickups, many=True)
        return Response(serializer.data)

    #function to get the list with the top 5 municipalities with the most polluted beaches
    @action(detail=True, methods=['GET'])
    def contaminatedMunicipalities(self, request):
        municipalities = Beach.objects.filter(num_residues__gt=0).order_by('num_residues').distinct()[:5]
        serializer = BeachSerializer(municipalities, many=True)
        return Response(serializer.data)