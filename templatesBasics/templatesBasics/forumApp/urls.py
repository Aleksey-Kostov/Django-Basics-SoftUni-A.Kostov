from django.urls import path
from templatesBasics.forumApp.views import dashboard, index

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dash'),
]