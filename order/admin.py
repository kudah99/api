from django.contrib import admin

from .models import Order, OrderItem


class orderItem(admin.ModelAdmin):

    list_display = fields = (
            "order",
            "product",
            "price",
            "quantity",
            "pharmacy"
        )
    search_fields = ('pharmacy__startswith',)
class order(admin.ModelAdmin):
    list_display = fields = (
            "order_number",
            "first_name",
            "last_name",
            "email",
            "address",
            "zipcode",
            "place",
            "phone",
            "paid_amount",
            "payment_methods",
            "poll_url",
            "medical_aid_image_url",
    )
    search_fields = ('place__startswith',)
    list_filter = ("created_at",)


admin.site.register(OrderItem,orderItem)
admin.site.register(Order,order)