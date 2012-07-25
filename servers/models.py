from django.db import models

class Server(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    ip_address = models.CharField(max_length=200)
    state = models.IntegerField()
    enabled = models.BooleanField()
    up_duration = models.IntegerField(null=True, blank=True)
    last_start_time = models.DateTimeField(null=True, blank=True)
    root_pwd = models.CharField(max_length=200, null=True, blank=True)
    os_name = models.CharField(max_length=200, null=True, blank=True)
    os_type = models.CharField(max_length=200, null=True, blank=True)
    os_version = models.CharField(max_length=200, null=True, blank=True)
    os_arch = models.CharField(max_length=200, null=True, blank=True)
    cpu_number = models.IntegerField(null=True, blank=True)
    cpu_freq = models.IntegerField(null=True, blank=True)
    cpu_arch = models.CharField(max_length=200, null=True, blank=True)
    memory_size = models.IntegerField(null=True, blank=True)
    memory_free = models.IntegerField(null=True, blank=True)
    instances = models.CharField(max_length=1000, null=True, blank=True)
    repos = models.CharField(max_length=1000, null=True, blank=True)
    disks = models.CharField(max_length=1000, null=True, blank=True)
    nicks = models.CharField(max_length=1000, null=True, blank=True)
    vgs = models.CharField(max_length=1000, null=True, blank=True)
    instancehosts = models.CharField(max_length=1000, null=True, blank=True)
    def __unicode__(self):
        return self.name
