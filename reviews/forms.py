from django import forms
from .models import Review


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'rating', 'description']
        widgets = {
            'description': forms.TextInput(attrs={'rows': 3})
        }