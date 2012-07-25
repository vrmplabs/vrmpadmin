from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vrmp.views.home', name='home'),
    # url(r'^vrmp/', include('vrmp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/instances/instance/index/', 'instances.views.index'),
    url(r'^admin/instances/instance/add/index/', 'instances.views.add'),
    url(r'^admin/instances/instance/save/index/', 'instances.views.save'),
    url(r'^admin/floatingips/floatingip/index/', 'floatingips.views.index'),
    url(r'^admin/floatingips/floatingip/add/index/', 'floatingips.views.add'),
    url(r'^admin/floatingips/floatingip/save/index/', 'floatingips.views.save'),
    url(r'^admin/floatingips/floatingip/associate/index/', 'floatingips.views.associate'),
    url(r'^admin/floatingips/floatingip/associate_save/index/', 'floatingips.views.associate_save'),
    url(r'^admin/', include(admin.site.urls)),
)
