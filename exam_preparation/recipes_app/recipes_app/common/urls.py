from django.urls import path

from recipes_app.common import views

urlpatterns = [
    path('', views.home_page, name='home'),
]
