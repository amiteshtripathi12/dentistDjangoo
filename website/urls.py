from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('components.html',views.components, name='components'),
    path('location.html',views.location, name='location'),
    path('table',views.table, name='table'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
