#from django.contrib.auth.models import User

from django.db import models
from product.models import Product
from pharmarcies.models import PharmaciesBranchDetails


class Order(models.Model):
    order_number = models.CharField(max_length=15)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    payment_methods = models.CharField(max_length=100)
    poll_url = models.URLField(max_length=250,default='n/a')
    medical_aid_image_url = models.URLField(max_length=250,default='n/a')
    
    class Meta:
        ordering = ['-created_at',]
        verbose_name_plural  =  "Check Orders" 

    def __str__(self):
        return self.first_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    pharmacy = models.ForeignKey(PharmaciesBranchDetails, related_name="items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id
    class Meta:
        verbose_name_plural  =  "Check Orders Details" 