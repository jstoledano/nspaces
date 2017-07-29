from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

handler400 = 'blog.views.error500'
handler404 = 'blog.views.error404'
handler500 = 'blog.views.error500'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('authtools.urls')),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'', include('blog.uris')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
