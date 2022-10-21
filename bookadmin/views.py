from urllib import response
from django.shortcuts import render
from .models import*
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['POST'])
def api_reg(request):
    x = request.data
    obj = api(name=x['name'],email=x['email'],password=x['password']).save()
    return Response('heloo')
@api_view(['GET'])
def show(request):
    a = api.objects.all()
    b = [{'id':i.id,'name':i.name,'email':i.email,'password':i.password}for i in a]
    return Response({'diplay':b})
@api_view(['DELETE'])
def delete(request,id):
    api.objects.get(id=id).delete()
    return Response({'val':'deleted'})





