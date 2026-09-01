from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile

def user_can_edit(func):
    def wrapper(request, pk, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=pk)
        if request.user.id != profile.user.id and profile.role == 'user':
            return HttpResponse('You cant edit this profile.')
        return func(request, pk, *args, **kwargs)
    return wrapper