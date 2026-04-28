from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.name 
    
class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.price}"
    
class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return f"Table {self.number} - Seats: {self.seats}"
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('p', 'Pending'), 
        ('pr', 'Preparing'), 
        ('s', 'Served'), 
        ('c', 'Completed'),
    ]
    PAYMENT_CHOICES = [
        ('p', 'Pending'),   
        ('c', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='p', null=True, blank=True)
    payment_status = models.CharField(max_length=5, choices=PAYMENT_CHOICES, null=True, blank=True)
    total_price = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)

    def __str__(self):
        return f"Order {self.id} - Table {self.table.number} - Total: {self.total_price}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items')
    menu_item = models.ForeignKey(Menu, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} - {self.price}"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    number_of_people = models.IntegerField()

    def __str__(self):
        return f"Reservation for {self.user.username} at Table {self.table.number} on {self.date_time}"
    
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} for Order {self.order.id}"
    