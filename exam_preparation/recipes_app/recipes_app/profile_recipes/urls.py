from django.urls import path, include

from recipes_app.profile_recipes import views

urlpatterns = [
    path('add/', views.create_profile, name='create-profile'),
    path('edit/', views.edit_profile, name='edit-profile'),
    path('delete/', views.delete_profile, name='delete-profile'),
    path('details', views.details_profile, name='details-profile')
]
