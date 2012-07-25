from django.conf.urls import patterns, include, url

urlpatterns = patterns('instances.views',
    url(r'^$', 'index'),
)
