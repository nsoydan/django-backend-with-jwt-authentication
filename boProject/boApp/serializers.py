from rest_framework import serializers
from .models import Bakim_List

class BakimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bakim_List
        fields = '__all__'

 