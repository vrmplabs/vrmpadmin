from django.contrib import admin
from servers.models import Server

class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip_address')

admin.site.register(Server, ServerAdmin)
