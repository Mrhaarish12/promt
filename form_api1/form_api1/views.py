import imp
from form_api1.models import Promotionfmodel
from form_api1.serialize import Promotionfserialize
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['POST'])
def savepromf(request):
    if request.method=="POST":
        saveserialze = Promotionfserialize(data=request.data)
        if saveserialze.is_valid():
            saveserialze.save()
            return Response(saveserialze.data, status=status.HTTP_201_CREATED)
            return Response(saveserialze.data,status=status.HTTP_400_BAD_REQUEST)