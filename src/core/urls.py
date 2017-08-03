from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

handler400 = 'apps.blog.views.error500'
handler404 = 'apps.blog.views.error404'
handler500 = 'apps.blog.views.error500'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^draceditor/', include('draceditor.urls')),
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    url(r'^accounts/', include('authtools.urls')),
    url(r'', include('apps.blog.uris')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
