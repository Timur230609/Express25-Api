from django.contrib import admin
from .models import Delivery
from .models import Review

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'courier', 'delivery_time', 'delivered_at')  
    search_fields = ('order', 'courier') 
    list_filter = ('delivered_at',)  
    ordering = ('-delivered_at',)  

admin.site.register(Delivery, DeliveryAdmin)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'product_name', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('customer_name', 'product_name', 'review_text')
    ordering = ('-created_at',)
