from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('books_api.urls')),
    # path('api/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
