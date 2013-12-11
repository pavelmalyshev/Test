from django.db import models
import datetime
from django.utils import timezone
from django.forms import ModelForm

    
class Autor(models.Model):
    fio = models.CharField(max_length=200)
    date_birth = models.DateField('date birthday')
    bio = models.CharField(max_length=5000)
    
    def __unicode__(self):
        return self.fio


class Stat(models.Model):
    date_pub = models.DateTimeField('date published')
    name = models.CharField(max_length=200)
    about = models.TextField(max_length=1000, null=True)
    text = models.TextField(max_length=5000)
    autor = models.ForeignKey(Autor)
    
    def __unicode__(self):
        return self.name


class Comment(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    who = models.CharField(max_length=200)
    text = models.TextField(max_length=5000)
    stat = models.ForeignKey(Stat)
    
    def __unicode__(self):
        return self.who
