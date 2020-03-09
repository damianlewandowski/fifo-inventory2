from rest_framework import serializers
from .models import Sold, Bought


class BoughtSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bought
        fields = ('date', 'quantity', 'cost_per_item')


class SoldSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sold
        fields = ('date', 'quantity', )


