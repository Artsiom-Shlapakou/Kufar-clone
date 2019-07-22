from django.urls import path
from . import views

urlpatterns = [
    path('countries/', views.CountryList.as_view()),
    path('countries/<int:pk>/', views.CountryDetail.as_view()),
    path('cities/', views.CityList.as_view()),
    path('cities/<int:pk>/', views.CityDetail.as_view()),
]