from django.contrib import admin
from floatingips.models import Floatingip

class FloatingipAdmin(admin.ModelAdmin):
    fields = ['pool']
    list_display = ('ip', 'instance_id', 'pool', 'action_html')

admin.site.register(Floatingip, FloatingipAdmin)
