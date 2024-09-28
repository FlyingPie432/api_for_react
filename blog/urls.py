from django.urls import path
from .views import BlogPostListCreateView, BlogPostDetailView

urlpatterns = [
    path('blog/', BlogPostListCreateView.as_view(), name='blogpost-list-create'),
    path('blog/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost-detail'),
]
