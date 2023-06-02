from django.forms import ModelForm
from django.forms.widgets import DateInput
from .models import Category, Clients, Orders, Products, Supplier

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ("id", "name")

class ClientsForm(ModelForm):
    class Meta:
        model = Clients
        fields = ("id", "first_name", "last_name", "birthdate", "address", "email", "password")
        widgets = {
            "birthdate": DateInput(attrs={"type": "date"})
        }

class OrdersForm(ModelForm):
    class Meta:
        model = Orders
        fields = ("id", "client_id", "order_date", "product_id", "quantity", "delivery_date")
        widgets = {
            "order_date": DateInput(attrs={"type": "date"}),
            "delivery_date": DateInput(attrs={"type": "date"})
        }

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ("id", "name", "color", "size", "price", "stock", "category_id", "supplier_id")

class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ("id", "name", "address", "contact_number")
