from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('WebProject.common.urls')),
    path('recipe/', include('WebProject.recipes.urls')),
    path('profile/', include('WebProject.profiles.urls')),
]
