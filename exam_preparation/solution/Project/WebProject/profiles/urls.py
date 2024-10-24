from django.urls import path
from WebProject.profiles import views

urlpatterns = [
    path('create/', views.create_profile_page, name='create-profile'),
    path('details/', views.profile_details_page, name='profile-details'),
    path('edit/', views.edit_profile_page, name='edit-profile'),
    path('delete/', views.delete_profile_page, name='delete-profile'),
]
