from django.contrib import admin
from .models import Customer, Bill, Product, ProductType, Order

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_filter = ["first_name", "last_name"]
    list_display = ["last_name", "account"]




    fieldsets = [
        (
            None,
            {
                "fields": ["first_name", "last_name"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["newsletter_abo"],
            },
        ),
    ]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Bill)
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(Order)