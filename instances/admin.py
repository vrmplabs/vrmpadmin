from django.contrib import admin
from instances.models import Instance

class InstanceAdmin(admin.ModelAdmin):
    fields = ['name', 'image', 'flavor']
    list_display = ('id', 'name', 'image', 'flavor')

admin.site.register(Instance, InstanceAdmin)
