from django.contrib import admin
from django.urls import path, include
import mainapp.views as mainapp

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', mainapp.Main.as_view(), name='main'),
    path('contacts/', mainapp.contacts, name='contacts'),
    path('catalog/', include('mainapp.urls', namespace='catalog')),

    path('api/slider/', mainapp.main_slider, name='slider'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
