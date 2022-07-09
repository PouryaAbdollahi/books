from django.shortcuts import render
from django.db.models import Q
from books.models import Book, Review
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from books.forms import CreateReviewForm
# Create your views here.


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    login_url = 'account_login'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['review_from'] = CreateReviewForm()
        return data

    def post(self, request, *args, **kwargs):
        _review = Review(
            book=self.get_object(),
            content=request.POST.get('content'),
            author=request.user
        )
        _review.save()
        return self.get(self, request, *args, **kwargs)


class SearchListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'pages/search-result.html'
    login_url = 'account_login'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        ).distinct()

