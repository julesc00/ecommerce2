from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Product, Order, OrderItem, ShippingAddress, Review


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serialize the user object."""


class ProductSerializer(serializers.ModelSerializer):
    """Serialize the product object."""
    class Meta:
        model = Product
        fields = "__all__"
