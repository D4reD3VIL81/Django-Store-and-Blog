from django.contrib import admin
from django.urls import path,include
from .views import *
from .forms import *

urlpatterns = [
    path('detail/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('list/', PostListView.as_view(), name='post-list'),
    path('add/',PostCreationForm.as_view(), name='post-create'),
    path('update-or-delete/<int:pk>/',PostDeleteOrUpdateFormView.as_view(),name='post-update-or-delete')
    
]