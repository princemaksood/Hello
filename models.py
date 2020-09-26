from django.db import models
from timezone_field import TimeZoneField

class Member(models.Model):
   id = models.CharField(max_length=20,blank=True,primary_key=True)
   real_name = models.CharField(max_length=20)
   tz = TimeZoneField(default='Europe/London')


class Period(models.Model):
   member = models.ForeignKey(Member, on_delete=models.CASCADE)
   start = models.DateTimeField()
   end = models.DateTimeField()




