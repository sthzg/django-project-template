from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(                                                               # /admin/
        r'^admin/',
        include(admin.site.urls)
    ),
]

if settings.DEBUG:
    urlpatterns = patterns(
        '',
        url(                                                          # /media/*
            r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}
        ),

        url(
            r'',
            include('django.contrib.staticfiles.urls')
        ),
    ) + urlpatterns
