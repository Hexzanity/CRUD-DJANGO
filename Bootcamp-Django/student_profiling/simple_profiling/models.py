from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Supplier(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    contact_number = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Suppliers"

    def __str__(self):
        return self.name


class Products(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


class Clients(BaseModel):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    birthdate = models.DateField()
    address = models.CharField(max_length=500)
    email = models.CharField(max_length=300)
    password = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "Clients"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Orders(BaseModel):
    id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    order_date = models.DateField()
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    delivery_date = models.DateField()

    class Meta:
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order #{self.id}"
