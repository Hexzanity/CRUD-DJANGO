from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.generic import DeleteView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login


from simple_profiling.models import Category, Clients, Orders, Products, Supplier
from simple_profiling.forms import CategoryForm, ClientsForm, OrdersForm, ProductsForm, SupplierForm

#ITO AY PARA SA CATEGORY
class CategoryList(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'category-list.html'
    
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    context_object_name = 'category'
    template_name = 'category-update.html'
    success_url = "/categories/"

    def form_valid(self, form):
        messages.success(self.request, "Category was updated successfully!")
        return super().form_valid(form)

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(request, "Category was deleted successfully!")
        return super().delete(request, *args, **kwargs)


#ITO AY PARA SA CLIENT

class ClientUpdateView(UpdateView):
    model = Clients
    form_class = ClientsForm
    context_object_name = 'client'
    template_name = 'client-update.html'
    success_url = "/clients/"

    def form_valid(self, form):
        messages.success(self.request, "Client was updated successfully!")
        return super().form_valid(form)

class ClientDeleteView(DeleteView):
    model = Clients
    template_name = 'clients_confirm_delete.html'
    success_url = reverse_lazy('client-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(request, "Client was deleted successfully!")
        return super().delete(request, *args, **kwargs)

#ITO AY PARA SA ORDER

class OrderUpdateView(UpdateView):
    model = Orders
    form_class = OrdersForm
    context_object_name = 'order'
    template_name = 'order-update.html'
    success_url = '/orders/'

def form_valid(self, form):
    # Retrieve the client object based on the client ID in the form
    client_id = form.cleaned_data.get('client')
    client_obj = Clients.objects.get(pk=client_id)

    # Update the form's instance with the client object
    self.object.client = client_obj

    messages.success(self.request, "Order was updated successfully!")
    return super().form_valid(form)


    

class OrderDeleteView(DeleteView):
    model = Orders
    template_name = 'order_confirm_delete.html'
    success_url = reverse_lazy('order-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(request, "Order was canceled successfully!")
        return super().delete(request, *args, **kwargs)

#ITO AY PARA SA PRODUCTS

class ProductUpdateView(UpdateView):
    model = Products
    form_class = ProductsForm
    context_object_name = 'product'
    template_name = 'product-update.html'
    success_url = "/products/"
    

    def form_valid(self, form):
        messages.success(self.request, "Product was updated successfully!")
        return super().form_valid(form)

class ProductDeleteView(DeleteView):
    model = Products
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(request, "Product was deleted successfully!")
        return super().delete(request, *args, **kwargs)

#ITO AY PARA SA SUPPLIER

class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm
    context_object_name = 'supplier'
    template_name = 'supplier-update.html'
    success_url = "/suppliers/"

    def form_valid(self, form):
        messages.success(self.request, "Supplier was updated successfully!")
        return super().form_valid(form)

class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'supplier_confirm_delete.html'
    success_url = reverse_lazy('supplier-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(request, "Supplier was deleted successfully!")
        return super().delete(request, *args, **kwargs)

#IBANG FUNCTIONS!

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category was added successfully!")
            return redirect('category-list')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

def add_client(request):
    if request.method == 'POST':
        form = ClientsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Client was added successfully!")
            return redirect('client-list')
    else:
        form = ClientsForm()
    return render(request, 'add_client.html', {'form': form})

def add_order(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Order was added successfully!")
            return redirect('order-list')
    else:
        form = OrdersForm()
    return render(request, 'add_order.html', {'form': form})

def add_product(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product was added successfully!")
            return redirect('product-list')
    else:
        form = ProductsForm()
    return render(request, 'add_product.html', {'form': form})

def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Supplier was added successfully!")
            return redirect('supplier-list')
    else:
        form = SupplierForm()
    return render(request, 'add_supplier.html', {'form': form})

class ClientList(ListView):
    model = Clients
    context_object_name = 'clients'
    template_name = 'client-list.html'

from django.db.models import F

class OrderList(ListView):
    model = Orders
    context_object_name = 'orders'
    template_name = 'order-list.html'

    def get_queryset(self):
        orders = super().get_queryset()
        orders = orders.select_related('client_id', 'product_id')
        return orders


class SupplierList(ListView):
    model = Supplier
    context_object_name = 'suppliers'
    template_name = 'supplier-list.html'

class ProductList(ListView):
    model = Products
    context_object_name = 'products'
    template_name = 'product-list.html'
    
    def get_queryset(self):
        products = super().get_queryset()
        products = products.select_related('category_id','supplier_id')
        return products

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if username == 'admin' and password == 'admin01':
            request.session['is_logged_in'] = True
            return redirect('category-list')
        
        error_message = "Invalid login credentials. Please try again."
        return render(request, 'login.html', {'error_message': error_message})
    
    else:
        return render(request, 'login.html')

