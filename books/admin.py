from django.contrib import admin
from django.contrib.admin import register
from books.models import Book, Review
# Register your models here.


class ReviewInline(admin.TabularInline):
    model = Review


@register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
    search_fields = ('title', 'author')
    inlines = [ReviewInline]