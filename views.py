from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework  import viewsets
from .Serializers import periodSerializer,memberSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from.models import *
from rest_framework import status
# Create your views here.


class memeberView(APIView):
    def get(self,request):
        queryset= Member.objects.all()
        serializer=memberSerializer(queryset,many=True)
        queryset1=Period.objects.all()
        serializer=periodSerializer(queryset1,many=True)
        return Response(serializer.data)
        return Response(serializer.data)