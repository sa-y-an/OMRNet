from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path
from django.contrib.auth import views as auth_views
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('predict/', include('classifier.urls')),
    path('api/', include('api.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

