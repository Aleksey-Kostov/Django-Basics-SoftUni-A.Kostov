from django.urls import path, include

from regular_exam_2024_feb.car.views import CreateCar, CarDetailView, EditCarView, DeleteCarView, catalogue_view

urlpatterns = [
    path('catalogue/', catalogue_view, name='catalog-page'),
    path('create/', CreateCar.as_view(), name='create-car'),
    path('<int:pk>/', include([
        path('details/', CarDetailView.as_view(), name='car-details'),
        path('edit/', EditCarView.as_view(), name='car-edit'),
        path('delete/', DeleteCarView.as_view(), name='car-delete'),
    ]))
]
