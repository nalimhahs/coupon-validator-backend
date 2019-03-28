from rest_framework import serializers

from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'name',
            'product',
            'phone',
            'email',
            'image',
            'college',
        )
