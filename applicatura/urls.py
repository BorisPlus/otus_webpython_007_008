from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.conf import settings
from django.views.static import serve

urlpatterns = []
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ]


urlpatterns += [
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'just_for_me/', admin.site.urls),
    url(r'rest_api/', include('api_ver_0_app.urls')),
    url(r'subscriber/', include('user_app.urls')),
    url(r'', include('dist_learn_app.urls')),
]
