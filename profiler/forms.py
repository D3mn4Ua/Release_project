from django import forms 


class UploadAvatarForm(forms.Form ):
    avatar = forms.ImageField(
    label = 'Download an avatar',
    required = False,
    widget = forms.ClearableFileInput(attrs ={'class':'form-control'})
    )
