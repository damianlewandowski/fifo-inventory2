from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from fifo_inventory.inventory.views.bought import BoughtViewSet
from fifo_inventory.inventory.views.sold import SoldViewSet
from fifo_inventory.inventory.views.inventory import inventory_status, inventory_value, inventory_item_value

router = DefaultRouter()
router.register(r'bought', BoughtViewSet)
router.register(r'sold', SoldViewSet)

urlpatterns = [
    path('quantity/', inventory_status, name='inventory_status'),
    path('value/', inventory_value, name='inventory_value'),
    path('item_value/', inventory_item_value, name='inventory_item_value'),
]

urlpatterns = format_suffix_patterns(urlpatterns)