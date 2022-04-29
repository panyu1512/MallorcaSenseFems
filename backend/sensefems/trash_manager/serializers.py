
from rest_framework import serializers
from .models import Trash

class TrashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trash
        fields = ['name', 'municipality', 'type_waste', 'num_residues', 'pickup_date', 'accepted']