from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('authtools.urls')),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'', include('blog.uris')),
]
