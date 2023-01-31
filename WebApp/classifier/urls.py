from django.urls import path, include
from . import views

app_name  = 'classifier'

urlpatterns = [
    path('', views.predict , name='predict'),

]
