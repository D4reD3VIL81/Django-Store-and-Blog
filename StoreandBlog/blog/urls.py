from django.contrib import admin
from django.urls import path,include
from .views import *

app_name = 'post'

urlpatterns = [
    path('<slug:slug>/', PostDetailView.as_view(), name='detail'),
    path('list/', PostListView.as_view(), name='list'),
    path('add/', PostCreateView.as_view(), name='add'),
    path('<slug:slug>/edit/', PostUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', PostDeleteView.as_view(), name='delete')
]