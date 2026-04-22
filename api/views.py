from rest_framework import generics
from .models import Product, Lead
from .serializers import ProductSerializer, LeadSerializer

# GET products (for slider)
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {'request': self.request}


# POST lead (from form)
class LeadCreateView(generics.CreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer