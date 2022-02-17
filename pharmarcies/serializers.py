from rest_framework import serializers
from pharmarcies.models import PharmaciesBranchDetails
from product.serializers import ProductSerializer

class PharmacyBranchSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)   
    class Meta:
        model = PharmaciesBranchDetails,
        fields = (
            "name",
            "country",
            "city",
            "email",
            "address",
            "whatsapp_contact",
            "phonenumbers"
        )