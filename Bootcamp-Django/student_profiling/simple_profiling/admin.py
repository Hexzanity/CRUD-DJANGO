from django.contrib import admin
from .models import Category, Clients, Orders, Products, Supplier

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "birthdate", "address", "email")
    search_fields = ("first_name", "last_name", "email")

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ("id", "client_id", "order_date", "product_id", "quantity", "delivery_date")
    search_fields = ("client_id__first_name", "client_id__last_name", "product_id__name")

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "color", "size", "price", "stock", "category_id", "supplier_id")
    search_fields = ("name", "category_id__name", "supplier_id__name")

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address", "contact_number")
    search_fields = ("name",)
