from django.urls import path
from vending import views

urlpatterns = [
    path('drinks/', views.DrinksView.as_view(), name="drinks"),
]
