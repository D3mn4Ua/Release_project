from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile
from products.models import Product
from blog.models import BlogAnnouncement
from django.contrib import messages

def user_can_edit(model):
    def decorator(func):
        def wrapper(request, pk, *args, **kwargs):
            obj = get_object_or_404(model, pk=pk)

            if isinstance(obj, Profile):
                if request.user.profile != obj.user.profile and request.user.profile.role == 'user':
                    messages.error(request, 'You can`t edit this profile.')
                    return redirect('401')

            if isinstance(obj, Product):
                if request.user.profile.role == 'user' and obj.seller != request.user.profile:
                    messages.error(request, 'You can`t edit this product.')
                    return redirect('401')
            
            if isinstance(obj, BlogAnnouncement):
                if request.user.profile.role == 'user' and obj.creator != request.user.profile:
                    messages.error(request, 'You can`t edit this announcement.')
                    return redirect('401')

            return func(request, pk, *args, **kwargs)
        return wrapper
    return decorator
