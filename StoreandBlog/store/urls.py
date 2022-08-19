from django.contrib import admin
from django.urls import path,include
from .views import *

app_name = 'store'

urlpatterns = [
    path('list/', ProductListView.as_view(), name= 'list-view'),
    path('<slug:slug>/', ProductDetailView.as_view, name= 'detail-view')
]