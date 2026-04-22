from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Product, Lead
from .serializers import ProductSerializer, LeadSerializer


# GET products (for slider)
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_serializer_context(self):
        return {'request': self.request}


# POST lead (from form)
@method_decorator(csrf_exempt, name='dispatch')
class LeadCreateView(generics.CreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [AllowAny]
