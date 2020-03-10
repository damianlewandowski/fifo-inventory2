import logging

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum, ExpressionWrapper, FloatField, F

from fifo_inventory.inventory.models import Bought
from fifo_inventory.inventory.serializers import BoughtSerializer

logger = logging.getLogger('fifo_inventory.inventory.views.bought')



class BoughtViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Bought.objects.all()
    serializer_class = BoughtSerializer

    @action(detail=False, methods=['get'])
    def quantity(self, request, format=None):
        total_quantity = Bought.objects.all().aggregate(Sum('quantity'))
        logger.info(f'Total quantity: {total_quantity}')
        return Response({'quantity': total_quantity['quantity__sum']})

    @action(detail=False, methods=['get'])
    def total_value(self, request, format=None):
        bought_price_total = Bought.objects.annotate(
            result=ExpressionWrapper(F('quantity') * F('cost_per_item'), output_field=FloatField())).aggregate(
            Sum('result'))
        return Response({'total_value': bought_price_total['result__sum']})