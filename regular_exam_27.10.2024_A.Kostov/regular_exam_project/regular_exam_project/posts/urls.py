from django.urls import path, include

from regular_exam_project.posts import views

urlpatterns = [
    path('create/', views.post_create, name='post-create'),
    path('<int:pk>/', include([
        path('details/', views.post_details, name='post-details'),
        path('edit/', views.post_edit, name='post-edit'),
        path('delete/', views.post_delete, name='post-delete'),
    ]))
]
