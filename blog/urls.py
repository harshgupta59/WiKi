from . import views
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView, 
    UserPostListView,
    RandomPostListView,
)

urlpatterns = [ 
    path('',PostListView.as_view(), name='blog-home'),
    path('random/',RandomPostListView.as_view(), name='random-post'),
    path('search/',views.SearchView, name='search'),
    path('announcements/',views.announcements, name='announcements'),
    path('user/<str:username>',UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    path('post/new/',PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]