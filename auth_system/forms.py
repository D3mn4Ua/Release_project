from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=63,
        required=False,
        widget=forms.TextInput(attrs={"class": "control-form", "placeholder": "Input your first-name (Optional)"})
    )
    second_name = forms.CharField(
        max_length=63,
        required=False,
        widget=forms.TextInput(attrs={"class": "control-form", "placeholder": "Input your second-name (Optional)"})
    )


    class Meta:
        model = User
        fields = ["username", "password1", "password2", "first_name", "second_name"]
        widgets = {"username": forms.TextInput(attrs={"class": "form-control"})}
    
    def __init__ (self, *args, **kwargs ):
        super ().__init__(*args, **kwargs )
        self.fields['password1'].widget = forms.PasswordInput(attrs ={'class':'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs ={'class':'form-control'})

