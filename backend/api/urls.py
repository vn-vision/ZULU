from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_index, name='index'),
    path('users/', views.UserView.as_view(), name='users'),
]