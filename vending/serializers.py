from rest_framework import serializers
from vending.models import Drinks


class DrinksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drinks
        fields = ('id', 'name', 'price', 'src', 'hot_flag', 'soda_flag', 'created_at', 'updated_at',)
