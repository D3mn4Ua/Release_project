from django import forms
from .models import BlogAnnouncement


class AnnouncementCreationForm(forms.ModelForm):
    class Meta:
        model = BlogAnnouncement
        fields = ['title', 'content', 'title_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'control-form'}),
            'content': forms.TextInput(attrs={'class': 'control-form', 'rows': 4}),
            'title_image': forms.ClearableFileInput()
        }