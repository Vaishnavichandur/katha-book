from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customers_list_create, name='customers_list_create'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customers/<int:pk>/payments/', views.add_payment, name='add_payment'),
    path('customers/export/', views.export_customers_excel, name='export_customers_excel'),
]
