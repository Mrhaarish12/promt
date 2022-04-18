from asyncore import read
from email import header
import imp
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

import requests
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
        
# def insertpromf(request):
#     if request.method=="POST":
#         pname=request.POST.get('pname')
#         pemail=request.POST.get('pemail')
#         pusername=request.POST.get('pusername')
#         data={'pname':pname,'pemail':pemail,'pusername': pusername}
#         headers={'Content-Type': 'application/json'}
#         read=requests.post('http://127.0.0.1:8000/promotform1', json=data,headers=headers)
#         t = loader.get_template('insert.html')
#         # return render(request,'insert.html')
#         return HttpResponse(t.render({},request))
#     else:
#         t = loader.get_template('insert.html')
#         # return render(request,'insert.html')
#         return HttpResponse(t.render({},request))