from django.conf.urls import patterns, url


urlpatterns = patterns('doubankong.access.views',
    url('^login/$', 'login'),
    url('^callback/$', 'callback'),
)
