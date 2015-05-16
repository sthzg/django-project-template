from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [

    url(                                                            # /api/v1/*/
        r'^api/v1/',
        include('service.apiurls', namespace='service-api')
    ),

    url(                                                            # /api-auth/
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),

    url(                                                      # /api-token-auth/
        r'^api-token-auth/',
        'rest_framework_jwt.views.obtain_jwt_token'
    ),

    url(                                                           # /apidocs/*/
        r'^apidocs/',
        include('rest_framework_swagger.urls')
    ),

    url(                                                                   # /*/
        r'^',
        include('service.urls', namespace='service')
    ),

    url(                                                             # /admin/*/
        r'^admin/',
        include(admin.site.urls)
    ),
]

if settings.DEBUG:
    urlpatterns = patterns(
        '',
        url(                                                         # /media/*/
            r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}
        ),

        url(
            r'',
            include('django.contrib.staticfiles.urls')
        ),
    ) + urlpatterns
