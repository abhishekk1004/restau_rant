from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f"Table {self.number}"

class Menu(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='menus', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    table = models.ForeignKey(Table, related_name='orders', on_delete=models.CASCADE)
    menu = models.ManyToManyField(Menu)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"Order {self.id} - Table {self.table.number}"
    
class Waiter(models.Model):
    name = models.CharField(max_length=100)
    orders = models.ManyToManyField(Order, related_name='waiters')

    def __str__(self):
        return self.name

class Reception(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
