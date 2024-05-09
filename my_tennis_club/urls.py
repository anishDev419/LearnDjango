
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path("", include('cbv.urls', namespace='cbv')),
    path("", include('routertest.urls')),
    # path("admin/", admin.site.urls),
    # path("books/", include('books.urls', namespace='books')),
]


if settings.DEBUG:
    urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))