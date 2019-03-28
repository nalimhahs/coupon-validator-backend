from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.OrderView.as_view(), name='coupon_verify')
]