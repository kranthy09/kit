from essentails.models import Form
from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('form/', views.FormList.as_view()),
    path('form/<int:pk>/', views.FormDetail.as_view()),
    path('brand/', views.BrandList.as_view()),
    path('brand/<int:pk>/', views.BrandDetail.as_view()),
    path('item/', views.ItemList.as_view()),
    path('item/<int:pk>/', views.ItemDetail.as_view()),
    path('useriteminfo/', views.UserItemInfoList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)