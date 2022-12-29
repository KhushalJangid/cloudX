from django.db import models
from Accounts.models import User
from os import path,remove
from cloudX.settings import MEDIA_ROOT
from cloudX.settings import domain

_types = [
    ('sports','Sports'),
    ('tech','Technical'),
    ('cultural','Cultural'),
    ('other','Other'),
]

# Create your models here.

class Data(models.Model):
    title = models.CharField(max_length=225)
    user = models.ForeignKey(to = User,on_delete=models.CASCADE)
    description = models.TextField(null=True,blank=True)
    link = models.TextField(null=True,blank=True)
    type = models.CharField(max_length=10,choices=_types)
    file = models.FileField(upload_to='data/')
    date = models.DateField()
    
    def extension(self):
        name, extension = path.splitext(self.file.name)
        return extension
    
    def delete(self, *args, **kwargs):
        remove(path.join(MEDIA_ROOT, self.file.name))
        super(Data,self).delete(*args,**kwargs)
