from django import forms
from .models import Product_test


class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product_test
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }

# class ImageCreationForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ['image', 'title_image']
#         widgets = {
#             'image': forms.ClearableImageField()
#         }