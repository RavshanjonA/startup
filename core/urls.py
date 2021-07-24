
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from .yasg import urlpatterns as doc_url


urlpatterns = doc_url+ [
    path('admin/', admin.site.urls),
    path('', include('basic.urls')),
    path('api/v1/', include('api.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', include('basic.urls')),
    path('api/v1/', include('api.urls')),

)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)