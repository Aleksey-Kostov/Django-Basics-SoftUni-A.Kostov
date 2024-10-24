from django.urls import path, include

from recipes_app.recipe import views

urlpatterns = [
    path('catalogue/', views.catalogue, name='catalogue'),
    path('create/', views.recipe_create, name='create-recipe'),
    path('<int:pk>/', include([
        path('edit/', views.edit_page, name='edit-page'),
        path('details/', views.recipe_details, name='details-recipe'),
        path('delete/', views.delete_recipe, name='delete-recipe'),
    ]))
]
