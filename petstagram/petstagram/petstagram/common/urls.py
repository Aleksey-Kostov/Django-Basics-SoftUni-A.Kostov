from django.urls import path

from petstagram.common import views

urlpatterns = (path('', views.homepage, name='homepage'),)
