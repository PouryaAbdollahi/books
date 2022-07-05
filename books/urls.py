from books.views import BookListView, BookDetailView
from django.urls import path


app_name = 'books'
urlpatterns = [
    path('', BookListView.as_view(), name='all-books'),
    path('<int:pk>/', BookDetailView.as_view(), name='detail')
]