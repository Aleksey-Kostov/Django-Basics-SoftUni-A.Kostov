from django.urls import path, include

from regular_exam_2024_feb.profile_car import views

urlpatterns = [
    path('create/', views.AlbumCreateView.as_view(), name='create-profile'),
]