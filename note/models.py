from django.db import models
import datetime
from django.utils import timezone

class Autor(models.Model):
    fio = models.CharField(max_length=200)
    date_birth = models.DateTimeField('date birthday')
    bio = models.CharField(max_length=5000)
    def __unicode__(self):
        return self.fio
	
class Stat(models.Model):
    date_pub = models.DateTimeField('date published')
    name = models.CharField(max_length=200)
#    about = models.CharField(max_length=1000, null=True)
    text = models.CharField(max_length=5000)
    autor = models.ForeignKey(Autor)
    
    def __unicode__(self):
        return self.name
    