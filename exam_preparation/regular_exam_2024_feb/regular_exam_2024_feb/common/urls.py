from django.urls import path, include

from regular_exam_2024_feb.common import views
from regular_exam_2024_feb.common.views import home_page

urlpatterns = [
    path('', home_page, name='home'),
]
