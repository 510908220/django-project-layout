from rest_framework import serializers

from .models import Shop


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ('id', 'name', 'category', 'status', 'created')
