from django.db import models

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
    