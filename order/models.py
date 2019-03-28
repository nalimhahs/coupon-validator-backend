from django.db import models

# Create your models here.

class Order(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    college = models.TextField()
    product = models.TextField()
    phone = models.TextField()
    email = models.EmailField()
    image = models.ImageField()
    status = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    lastUpdated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' ' + self.product

    class Meta:
        unique_together = ['email', 'phone']