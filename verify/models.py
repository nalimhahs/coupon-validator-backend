from django.db import models

# Create your models here.

class Coupon(models.Model):
    coupon = models.CharField(max_length= 20, unique= True)
    discount = models.IntegerField()
    created = models.DateField(auto_now_add=True)
    expiry = models.DateField()

    class Meta:
        unique_together = ['coupon', 'discount']

    def __str__(self):
        return self.coupon
