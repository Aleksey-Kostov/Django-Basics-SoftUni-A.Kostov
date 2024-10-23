from django.urls import path

from regular_exam_2024_feb.profile_car import views
from regular_exam_2024_feb.profile_car.views import profile_detail, edit_profile, delete_profile, create_profile

urlpatterns = [
    path('create/', create_profile, name='create-profile'),
    path('details/', profile_detail, name='profile-details'),
    path('edit/', edit_profile, name='profile-edit'),
    path('delete/', delete_profile, name='profile-delete'),
]
