from django.db import models
from django.contrib.auth.models import User
from servers.models import Server
from instances.models import Instance

class Log(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    server = models.ForeignKey(Server)
    instance = models.ForeignKey(Instance)
    info = models.CharField(max_length=200)
    create_time = models.DateTimeField()
    def __unicode__(self):
        return self.info
