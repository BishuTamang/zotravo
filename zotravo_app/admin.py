from django.contrib import admin
from .models import Product, ProductImage, Partner, Orders


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'room_type')  # Add fields to be displayed in the list view
    search_fields = ('name', 'room_type')  # Add fields to be searchable


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name')
    search_fields = ('first_name',)


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_date')  # Add fields to be displayed in the list view
    search_fields = ('create_date', 'name')  # Add fields to be searchable


admin.site.register(Product)
admin.site.register(ProductImage)
# admin.site.register(CustomUser)
admin.site.register(Partner)
admin.site.register(Orders)
