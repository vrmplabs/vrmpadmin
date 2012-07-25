from django.db import models

class Pool(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Floatingip(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    ip = models.CharField(max_length=200)
    pool = models.ForeignKey(Pool, null=True, blank=True)
    instance_id = models.CharField(max_length=200, null=True, blank=True)
    def action_html(self):
        html = ''
        if not self.instance_id:
            html = '<a href="/admin/floatingips/floatingip/associate/index/?ip=%s">Associate IP</a>' % self.ip
        return html
    action_html.short_description = 'actions'
    action_html.allow_tags = True
    def __unicode__(self):
        return self.ip
