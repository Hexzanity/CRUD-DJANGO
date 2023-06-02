from django.urls import path
from simple_profiling.views import (
    CategoryList,
    CategoryUpdateView,
    CategoryDeleteView,
    ClientList,
    ClientUpdateView,
    ClientDeleteView,
    OrderUpdateView,
    OrderDeleteView,
    ProductUpdateView,
    ProductDeleteView,
    SupplierUpdateView,
    SupplierDeleteView,
    add_category,
    add_client,
    add_order,
    add_product,
    add_supplier,
    ClientList, 
    OrderList, 
    SupplierList, 
    ProductList,
    login_view,

    
)

urlpatterns = [
    path('', login_view, name='login'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('clients/<int:pk>/update/', ClientUpdateView.as_view(), name='client-update'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('suppliers/<int:pk>/update/', SupplierUpdateView.as_view(), name='supplier-update'),
    path('suppliers/<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier-delete'),
    
    path('add_category/', add_category, name='add-category'),
    path('add_client/', add_client, name='add-client'),
    path('add_order/', add_order, name='add-order'),
    path('add_product/', add_product, name='add-product'),
    path('add_supplier/', add_supplier, name='add-supplier'),
    
    path('clients/', ClientList.as_view(), name='client-list'),
    path('orders/', OrderList.as_view(), name='order-list'),
    path('suppliers/', SupplierList.as_view(), name='supplier-list'),
    path('products/', ProductList.as_view(), name='product-list'),
]