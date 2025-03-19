from django.urls import path
from electronics import views

urlpatterns = [
    path('electronics/product/', views.product, name='electronics/product'),
    path('electronics/card/', views.card, name='electronics/card'),
]


