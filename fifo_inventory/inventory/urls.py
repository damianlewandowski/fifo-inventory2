from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from fifo_inventory.inventory import views

urlpatterns = [
    path('quantity/', views.inventory_status),
    path('value/', views.inventory_value),
    path('item_value/', views.inventory_item_value),
    # path('snippets/<int:pk>', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)