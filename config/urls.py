from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

from config import settings

urlpatterns = [
    path("", include("shortlinks.urls")),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
