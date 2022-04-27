from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Pigga Admin"
admin.site.site_title = "Pigga Admin Portal"
admin.site.index_title = "Welcome to Pigga Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls')),
]
