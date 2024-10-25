from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Delivery(models.Model):
    order = models.BigIntegerField()  
    courier = models.BigIntegerField()  
    delivery_time = models.BigIntegerField()  
    delivered_at = models.BigIntegerField()  

    class Meta:
        db_table = 'delivery'  
        verbose_name = 'Delivery'  
        verbose_name_plural = 'Deliveries'  
        ordering = ['-delivered_at'] 
    
    def __str__(self):
        return f"Delivery {self.id} for Order {self.order}"
    
    def clean(self):
        if self.delivered_at < self.delivery_time:
            raise ValidationError("Delivered time cannot be earlier than the delivery time.")
        if self.delivery_time <= 0:
            raise ValidationError("Delivery time must be a positive number.")
        if self.delivered_at <= 0:
            raise ValidationError("Delivered time must be a positive number.")

class Review(models.Model):
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name='reviews')  
    rating = models.IntegerField()  
    comment = models.TextField(blank=True)  
    created_at = models.DateTimeField(auto_now=True)  

    class Meta:
        db_table = 'review'  
        verbose_name = 'Review'  
        verbose_name_plural = 'Reviews'  
        ordering = ['-created_at'] 

    def __str__(self):
        return f"Review for Delivery {self.delivery.id} - Rating: {self.rating}"

    def clean(self):
        if self.rating < 1 or self.rating > 5:
            raise ValidationError("Rating must be between 1 and 5.")
