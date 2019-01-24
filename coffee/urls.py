from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view()),
    path('<int:pk>/', views.CoffeeDetailView.as_view()),
]
