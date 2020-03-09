from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from fifo_inventory.inventory import views
from fifo_inventory.inventory.views import BoughtViewSet, SoldViewSet

router = DefaultRouter()
router.register(r'bought', BoughtViewSet)
router.register(r'sold', SoldViewSet)

urlpatterns = [
    path('quantity/', views.inventory_status, name='inventory_status'),
    path('value/', views.inventory_value, name='inventory_value'),
    path('item_value/', views.inventory_item_value, name='inventory_item_value'),
]

urlpatterns = format_suffix_patterns(urlpatterns)