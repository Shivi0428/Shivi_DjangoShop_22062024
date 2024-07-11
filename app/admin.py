from django.utils.html import format_html
from django.urls import reverse
from django.contrib import admin
from .models import (
    Instance,
    Cart,
    OrderPlaced,
    Customer,
    Product,
    Sorder,
    Soitem,
    Static,
    V_Lorders,
    V_Loitems
)

# Register models without custom admin classes
admin.site.register(Instance)
admin.site.register(Sorder)
admin.site.register(Soitem)
admin.site.register(Static)
admin.site.register(V_Lorders)
admin.site.register(V_Loitems)

# Custom admin classes
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price',  'description', 'brand', 'category', 'product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'customer_info', 'product', 'product_info', 'quantity', 'ordered_date', 'status']

    def product_info(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)

    def customer_info(self, obj):
        link = reverse("admin:app_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer.name)
