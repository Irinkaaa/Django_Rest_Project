from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('books_api.urls')),
    # path('api/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
