from django.urls import path
from WebProject.common import views


urlpatterns = [
    path('', views.home_page, name='home'),
]