from rest_framework import serializers
from form_api1.models import Promotionfmodel

class Promotionfserialize(serializers.ModelSerializer):
    class Meta:
        model=Promotionfmodel
        fields="__all__"