from django.urls import path
from .views import BlogPostListCreateView, BlogPostDetailView, NewsListCreateView, NewsDetailView, ContactCreateView

urlpatterns = [
    path('blog/', BlogPostListCreateView.as_view(), name='blogpost-list-create'),
    path('blog/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('news/', NewsListCreateView.as_view(), name='news-list-create'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('contact/', ContactCreateView.as_view(), name='contact-create')
]
