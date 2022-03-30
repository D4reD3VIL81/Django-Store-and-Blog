from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('detail/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('list/', PostListView.as_view(), name='post-list'),
    path('add/', AuthorCreateView.as_view(), name='post-add'),
    path('<int:pk>/', AuthorUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete/', AuthorDeleteView.as_view(), name='post-delete'),
    
]