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

    # Handling neighborhood models / call to the neighborhood API
    path('neighborhoods/', views.NeighborhoodView.as_view(), name='neighborhoods-list'), # For GET and POST
    path('neighborhoods/<int:id>/', views.NeighborhoodView.as_view(), name='neighborhoods-detail'), # For PATCH and DELETE

    # Handling property models / call to the property API
    path('properties/', views.PropertyView.as_view(), name='properties-list'), # For GET and POST
    path('properties/<int:id>/', views.PropertyView.as_view(), name='properties-detail'), # For PATCH and DELETE

    # Handling market trend models / call to the market trend API
    path('market-trends/', views.MarketTrendView.as_view(), name='market-trends-list'), # For GET and POST
    path('market-trends/<int:id>/', views.MarketTrendView.as_view(), name='market-trends-detail'), # For PATCH and DELETE

    # Handling user feedback models / call to the user feedback API
    path('user-feedback/', views.UserFeedbackView.as_view(), name='user-feedback-list'), # For GET and POST
    path('user-feedback/<int:id>/', views.UserFeedbackView.as_view(), name='user-feedback-detail'), # For PATCH and DELETE

    # Handling prediction models / call to the prediction API
    path('predictions/', views.PredictionView.as_view(), name='predictions-list'), # For GET and POST
    path('predictions/property/<int:id>/', views.PredictionView.as_view(), name='property-predictions-detail'), # For PATCH and DELETE
    path('predictions/neighborhood/<int:id>/', views.PredictionView.as_view(), name='neighborhood-predictions-detail'), # For PATCH and DELETE
    

    # Handling property images models / call to the property images API
    path('property-images/', views.PropertyImageView.as_view(), name='property-images-list'), # For GET and POST
    path('property-images/<int:id>/', views.PropertyImageView.as_view(), name='property-images-detail'), # For PATCH and DELETE

]