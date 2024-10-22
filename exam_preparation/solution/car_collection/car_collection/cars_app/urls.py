from django.urls import path, include

from car_collection.cars_app.views import catalogue_page, create_car_page, edit_car_page, delete_car_page, \
    car_details_page

urlpatterns = [
    path('catalogue/', catalogue_page, name='catalogue'),
    path('create/', create_car_page, name='create-car'),
    path('<int:pk>/', include([
        path('edit/', edit_car_page, name='edit-car'),
        path('delete/', delete_car_page, name='delete-car'),
        path('details/', car_details_page, name='car-details'),
    ]))
]
