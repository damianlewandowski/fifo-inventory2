import datetime
import logging

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum, ExpressionWrapper, FloatField, F

from fifo_inventory.inventory.models import Bought, Sold


logger = logging.getLogger(__name__)

# Example:
# Question: How many pens does Sebastian have in stock ultimo Jan 11th 2016?
#
# Answer: Grab Bought and Sold models, take all of the rows ultimo Jan 11th 2016,
# subtract from Bought Sold and return the result
#
@api_view(['GET'])
def inventory_status(request, format=None):
    """
    How many pens in stock ultimo {year} {month} {day}
    """
    year = int(request.query_params['year'])
    month = int(request.query_params['month'])
    day = int(request.query_params['day'])

    ultimo = datetime.date(year, month, day)

    bought_items = Bought.objects.filter(date__lte=ultimo).aggregate(Sum('quantity'))
    sold_items = Sold.objects.filter(date__lte=ultimo).aggregate(Sum('quantity'))

    bought_items_sum = bought_items['quantity__sum']
    sold_items_sum = sold_items['quantity__sum']

    # This will be initial value if nothing was bought
    result = 0

    # If something was bought and nothing was sold
    if bought_items_sum is not None and sold_items_sum is None:
        result = bought_items_sum

    # If something was bought and sold
    elif bought_items_sum is not None and sold_items is not None:
        result = bought_items_sum - sold_items_sum

    logger.info(f'User bought: {bought_items}, sold: {sold_items} ultimo {ultimo}.')
    logger.info(f'There are {result} items left in his inventory.')

    return Response({'quantity': result})


# What is the value of the inventory ultimo Jan 11th 2016?
# Grab Bought and Sold models, grab earliest row from Sold, grab quantity from it, extract it from quantity from Bought
# date needs to be smaller, repeat this untill you have nothing in sold
# The value of inventory is eveyrthing that is an excess in Bought
@api_view(['GET'])
def inventory_value(request, format=None):
    """
    Total value of inventory ultimo {year} {month} {day}
    """
    year = int(request.query_params['year'])
    month = int(request.query_params['month'])
    day = int(request.query_params['day'])

    ultimo = datetime.date(year, month, day)

    # Total quantity of sold items ultimo {ultimo}
    sold_items_total_quantity = Sold.objects.filter(date__lte=ultimo).aggregate(Sum('quantity'))
    sold_items_total_quantity = sold_items_total_quantity['quantity__sum']

    # No sold items in requested ultimo
    if sold_items_total_quantity is None:
        sold_items_total_quantity = 0

    # Total value of inventory without selling anything ultimo {ultimo}
    # Might as well calculate it inside database since it's much more efficient
    bought_price_total = Bought.objects.filter(date__lte=ultimo).annotate(
        result=ExpressionWrapper(F('quantity') * F('cost_per_item'), output_field=FloatField())).aggregate(
        Sum('result'))
    bought_price_total = bought_price_total['result__sum']

    bought_items_set = Bought.objects.filter(date__lte=ultimo).order_by('date')

    # Use iterator to load data in chunks instead of all at once.
    # Protects from loading huge sets of data into memory at once
    for bought_item in bought_items_set.iterator():
        difference = sold_items_total_quantity - bought_item.quantity

        # More bought by given day than sold
        if difference < 0:
            bought_price_total -= sold_items_total_quantity * bought_item.cost_per_item
            break
        # Sold more
        else:
            bought_price_total -= bought_item.quantity * bought_item.cost_per_item
            sold_items_total_quantity -= bought_item.quantity

    logger.info(f'Current inventory value: {bought_price_total}')

    return Response({'inventory_value': bought_price_total})


# What are the costs of pen solds ultimo Jan 11th 2016?
@api_view(['GET'])
def inventory_item_value(request, format=None):
    """
    Value of item ultimo {year} {month} {day}
    """
    year = int(request.query_params['year'])
    month = int(request.query_params['month'])
    day = int(request.query_params['day'])

    ultimo = datetime.date(year, month, day)

    # Total quantity of sold items ultimo {ultimo}
    sold_items_total_quantity = Sold.objects.filter(date__lte=ultimo).aggregate(Sum('quantity'))
    sold_items_total_quantity = sold_items_total_quantity['quantity__sum']

    # No sold items in given ultimo
    if sold_items_total_quantity is None:
        sold_items_total_quantity = 0

    # All of the bought items ultimo {ultimo}
    bought_items_set = Bought.objects.filter(date__lte=ultimo).order_by('date')

    # Use iterator to load data in chunks instead of all at once.
    # Protects from loading huge sets of data into memory at once
    for bought_item in bought_items_set.iterator():
        difference = sold_items_total_quantity - bought_item.quantity

        # More bought by given day than sold
        if difference < 0:
            logger.info(f'Found current item cost: {bought_item.cost_per_item}')
            return Response({'current_item_price': bought_item.cost_per_item})
        # Sold more
        else:
            sold_items_total_quantity -= bought_item.quantity

    logger.error(f'Method not handling edge cases properly')
    return Response('Database might be empty.', status=status.HTTP_400_BAD_REQUEST)
