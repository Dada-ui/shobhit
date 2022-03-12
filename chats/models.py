from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class registermodel(User):
    phone=models.BigIntegerField()
    age=models.IntegerField()
    gender=models.CharField(max_length=10, choices=[['Male','MALE'],['Female','FEMALE']])
    pic=models.ImageField(upload_to='profile/')
    dor=models.DateTimeField(default=timezone.now)


class chatmodel(models.Model):
    cid=models.ForeignKey(registermodel,on_delete=models.CASCADE)
    msg=models.CharField(max_length=500)
    datetime=models.DateTimeField(default=timezone.now)
    cimg=models.ImageField(upload_to='chatimg/', null=True)
    cfile=models.FileField(upload_to='chatdoc/',null=True)