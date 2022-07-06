from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=128)
    cover = models.ImageField(upload_to='book_cover', blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:detail', args=[str(self.id)])


DEFAULT_REVIEW_ID = 1


class Review(models.Model):
    book = models.ForeignKey('Book', blank=True, null=True, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(
        get_user_model(),
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    def __str__(self):
        return self.content

