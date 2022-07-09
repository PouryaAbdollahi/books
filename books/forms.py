from django import forms
from books.models import Review


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'type you review'})
        }
        labels = {
            'content': ''
        }