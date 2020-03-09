from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from fifo_inventory.inventory.urls import router as inventory_router

router = DefaultRouter()
# router.registry.extend(inventory_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(inventory_router.urls)),
    path('api/v1/inventory/', include('fifo_inventory.inventory.urls')),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
