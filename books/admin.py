from django.contrib import admin
from django.contrib.admin import register
from books.models import Book
# Register your models here.


@register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
    search_fields = ('title', 'author')