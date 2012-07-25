from django.db import models
from django.contrib.auth.models import User

class Keypair(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    real_id = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    create_time = models.DateTimeField()
    def __unicode__(self):
        return self.name
