from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from app import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('goods.urls', namespace='catalog')),
    path('user/', include('users.urls', namespace='user')),
    path('cart/', include('carts.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('payments/', include('payments.urls',)),
]

if settings.DEBUG:
    urlpatterns += [
        
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""
www.site.com/admin/
www.site.com
www.site.com/about/
www.site.com/catalog/
www.site.com/catalog/product
"""