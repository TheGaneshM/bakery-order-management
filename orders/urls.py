from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('orders/', views.order_list, name='order_list'),
    path('add-order/', views.add_order, name='add_order'),
    path('update-order/<int:pk>/', views.update_order, name='update_order'),
    path('delete-order/<int:pk>/', views.delete_order, name='delete_order'),
]