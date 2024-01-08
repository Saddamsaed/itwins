from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import debug_toolbar

admin.site.site_header = 'Itwins Store'
admin.site.index_title = 'Management'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('api/v1/store/', include('store.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('api/v1/__debug__/', include(debug_toolbar.urls)),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

