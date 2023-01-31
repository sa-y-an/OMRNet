from .views import ImageCreate
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

app_name = 'api'

urlpatterns = [
    path('', ImageCreate.as_view(), name='list'),
]