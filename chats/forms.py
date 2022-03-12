from django.utils import timezone
from django import forms
from chats.models import *


class Chats_Form(forms.Form):
    msg=forms.CharField(max_length=500,required=False)
    datetime=forms.SplitHiddenDateTimeWidget()
    cimg=forms.ImageField(required=False)
    cfile=forms.FileField(required=False)