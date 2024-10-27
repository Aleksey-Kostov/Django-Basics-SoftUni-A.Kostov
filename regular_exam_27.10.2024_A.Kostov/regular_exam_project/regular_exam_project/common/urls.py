from django.urls import path

from regular_exam_project.common import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
