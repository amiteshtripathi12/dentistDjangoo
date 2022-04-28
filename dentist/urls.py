from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


admin.site.site_header = "Pigga Admin"
admin.site.site_title = "Pigga Admin Portal"
admin.site.index_title = "Welcome to Pigga Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}),
]
'''
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
'''