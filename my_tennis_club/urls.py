
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include('cbv.urls', namespace='cbv')),
    path("admin/", admin.site.urls),
    path("books/", include('books.urls', namespace='books')),
]
