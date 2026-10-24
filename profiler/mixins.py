from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages

def user_can_edit(func):
    def wrapper(request, pk, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=pk)
        if request.user.id != profile.user.id and request.user.profile.role == 'user':
            messages.error(request, 'You can`t edit this object. ')
            return redirect('401')
        return func(request, pk, *args, **kwargs)
    return wrapper