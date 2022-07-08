from books.views import BookListView, BookDetailView, SearchListView
from django.urls import path, re_path


app_name = 'books'
urlpatterns = [
    path('', BookListView.as_view(), name='all-books'),
    path('<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('search/', SearchListView.as_view(), name='search_result')
]
