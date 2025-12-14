from django.contrib import admin
from .models import Cart, CartItem, Order, DeliveryDetails

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['user__username']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['cart__user__username', 'product__name']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_amount', 'status', 'created_at']
    list_filter = ['status', 'created_at', 'updated_at']
    search_fields = ['user__username', 'delivery_details__full_name']
    readonly_fields = ['total_amount']

@admin.register(DeliveryDetails)
class DeliveryDetailsAdmin(admin.ModelAdmin):
    list_display = ['order', 'full_name', 'phone_number', 'city', 'state']
    search_fields = ['full_name', 'phone_number', 'email', 'city']
    list_filter = ['state', 'city'] 