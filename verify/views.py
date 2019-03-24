from rest_framework.views import APIView
from rest_framework.response import Response

from django.utils.datastructures import MultiValueDictKeyError

from . import models
from . import serializers

class CouponVerify(APIView):
    def get(self, request, format=None):
        try:
            coupon = models.Coupon.objects.get(coupon=request.query_params['coupon'])
        except (models.Coupon.DoesNotExist, MultiValueDictKeyError): 
            coupon = None
        serializer = serializers.CouponSerializer(coupon)
        return Response(serializer.data)