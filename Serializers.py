from rest_framework import serializers
from . models import *

class memberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Member
        fields=['id','real_name','tz']
class periodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Period
        fields="__all__"