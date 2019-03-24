from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.CouponVerify.as_view(), name='coupon_verify')
]