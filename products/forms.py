from django import forms
from .models import Product, Image


class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'quality', 'quantity', 'product_image', 'category', 'manufacturer']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'min': 1}),
            'quality': forms.Select(attrs={}),
            'quantity': forms.NumberInput(attrs={'min': 0})
        }

class ImageCreationForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'description']
        widgets = {
            'image': forms.ClearableFileInput(),
            'description': forms.TextInput(attrs={'rows': 6})
        }