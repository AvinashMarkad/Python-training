from django.urls import path
from electronics import views

urlpatterns = [
    path('electronics/product/', views.product, name='electronics/product'),
    path('electronics/card/', views.card, name='electronics/card'),
    path('delete_product/<int:id>/', views.delete_product, name='delete_product'),
    path('update_product/<int:id>/', views.update_product, name='update_product'),
]


