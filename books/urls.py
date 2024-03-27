from django.urls import path
from .views import IndexView, BookDetailView, BookListView, GenreView, AddFormView, BookEditView

app_name="books"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('list/', BookListView.as_view(), name='book-list'),
    path('add/', AddFormView.as_view(), name='add-book'),
    path('g/<str:genre>', GenreView.as_view(), name='book-list'),
    path('<slug:slug>/', BookDetailView.as_view(), name='book-detail'),
    path('<slug:slug>/edit/', BookEditView.as_view(), name='edit-detail'),
]