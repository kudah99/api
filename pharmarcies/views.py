from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import PharmacyBranchSerializer
from .models import PharmaciesBranchDetails


class GetProductsByCountry(APIView):
    def get_object(self,country):
        try:
            return PharmaciesBranchDetails.get(slug=country)
        except PharmaciesBranchDetails.DoesNotExist:
            raise Http404
