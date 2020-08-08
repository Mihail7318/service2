from django.urls import path

from . import views

urlpatterns = [
    path('city/', views.CityListView.as_view()),
    path('city/street/', views.StreetListView.as_view()),
    path('createshop/',views.ShopCreateView.as_view()),
    path('shop/',views.ShopView.as_view()),
]