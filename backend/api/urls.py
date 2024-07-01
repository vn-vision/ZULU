from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    # The default landing page for ZULU
    path('', views.api_index, name='index'),

    # Handling login and logout, session authentication
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), # For login using Django Rest Framework login view
    path('login/', auth_views.LoginView.as_view(), name='login'), # For login using Django built-in login view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # For logout using Django built-in logout view

    # Handling user models / call to the user API
    path('users/', views.UserView.as_view(), name='users-list'), # For GET and POST
    path('users/<int:id>/', views.UserView.as_view(), name='users-detail'), # For PATCH and DELETE

]