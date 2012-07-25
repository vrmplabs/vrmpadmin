from django.db import models
from servers.models import Server

class Image(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Flavor(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Instance(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=200)
    image = models.ForeignKey(Image, null=True, blank=True)
    flavor = models.ForeignKey(Flavor, null=True, blank=True)
    def __unicode__(self):
        return self.name
