from django.contrib import admin
from pharmarcies.models import PharmaciesBranchDetails#PharmaciesMananger


class pharmacyBranch(admin.ModelAdmin):

    list_display = fields = (
            "name",
            "country",
            "city",
            "email",
            "address",
            "whatsapp_contact",
            "phonenumbers",
           
        )
    search_fields = ('name__startswith',)
# class pharmacyManager(admin.ModelAdmin):

#     list_display = fields = (
#             "first_name",
#             "last_name",
#             "email",
#             "whatsapp_contact",
#             "phonenumbers",
#         )
#     search_fields = ('first_name__startswith',)
admin.site.register(PharmaciesBranchDetails,pharmacyBranch)
# admin.site.register(PharmaciesMananger,pharmacyManager)
