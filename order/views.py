from rest_framework import generics

# Create your views here.

from . import models
from . import serializers

class OrderView(generics.CreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer