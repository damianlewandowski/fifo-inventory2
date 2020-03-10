import logging

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum

from fifo_inventory.inventory.models import Bought, Sold
from fifo_inventory.inventory.serializers import SoldSerializer


logger = logging.getLogger(__name__)

class SoldViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Sold.objects.all()
    serializer_class = SoldSerializer

    def filter_queryset(self, queryset):
        queryset = super(SoldViewSet, self).filter_queryset(queryset)
        return queryset.order_by('date')

    @action(detail=False, methods=['get'])
    def total_value(self, request):
        all_sold_items = Sold.objects.aggregate(Sum('quantity'))
        all_sold_items = all_sold_items['quantity__sum']

        result = 0

        bought_items_set = Bought.objects.all()

        # Use iterator to load data in chunks instead of all at once.
        # Protects from loading huge sets of data into memory at once
        for bought_item in bought_items_set.iterator():
            difference = all_sold_items - bought_item.quantity

            # More bought by given day than sold
            if difference < 0:
                result += all_sold_items * bought_item.cost_per_item
                break
            # Sold more
            else:
                result += bought_item.quantity * bought_item.cost_per_item
                all_sold_items -= bought_item.quantity

        return Response({'total_value': result})