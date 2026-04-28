from django.contrib import admin

# Register your models here.
from .models import Menu, Order, OrderItem, Table, category
class categoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
admin.site.register(category, categoryAdmin)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category']
    search_fields = ['name',]
    list_filter = ['category']
admin.site.register(Menu, MenuAdmin)

class TableAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'seats', 'is_available']
    list_filter = ['is_available']
admin.site.register(Table, TableAdmin)

class OrderItemInline(admin.TabularInline):
    model = OrderItem

    list_display = ['id', 'order', 'menu_item', 'quantity', 'price']
    list_filter = ['order']
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'date', 'status', 'payment_status', 'total_price']
    list_filter = ['status', 'payment_status']
    search_fields = ['user_username',]
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)

