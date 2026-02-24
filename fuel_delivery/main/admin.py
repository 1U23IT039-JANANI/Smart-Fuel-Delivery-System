from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'fuel_type', 'liters', 'status', 'created_at')
    list_filter = ('status', 'fuel_type')
    search_fields = ('user__username', 'address', 'phone')

admin.site.register(Order, OrderAdmin)