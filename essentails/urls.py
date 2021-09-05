from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form_list),
    path('form/<int:pk>/', views.form_detail),
]