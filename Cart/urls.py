from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from product_app import views as prod_views
from user_app import views as user_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('models', prod_views.ProductApiView)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
     path('api/', include('rest_framework.urls')),
    path('accounts/', include('allauth.urls')),
    path('', prod_views.product_list, name='home'),
    path('detail/<int:product_id>', prod_views.detail_view, name='detail'),
    
    
    
    
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]

