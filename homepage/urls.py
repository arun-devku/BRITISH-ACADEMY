from django.urls import path
from homepage import views


urlpatterns = [
path('index2', views.index2,name='index2'),
]