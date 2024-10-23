from django.urls import path, include

from regular_exam_2024_feb.car import views
from regular_exam_2024_feb.car.views import CatalogueView

urlpatterns = [
    path('catalogue/', CatalogueView.as_view(), name='catalog-page')
]
