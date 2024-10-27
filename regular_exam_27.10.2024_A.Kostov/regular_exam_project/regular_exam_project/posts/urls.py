from django.urls import path, include

from regular_exam_project.posts import views
from regular_exam_project.posts.views import PostDetailView

urlpatterns = [
    path('create/', views.post_create, name='post-create'),
    path('<int:pk>/', include([
        path('details/', PostDetailView.as_view(), name='post-details'),
        path('edit/', views.post_edit, name='post-edit'),
        path('delete/', views.post_delete, name='post-delete'),
    ]))
]
