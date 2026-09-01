from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm
from .models import Profile
from .mixins import user_can_edit

@login_required
def view_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    profile.auto_give_role
    return render(request, 'profile/view_profile.html', {'profile': profile})

@login_required
@user_can_edit
def edit_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk )
    profile.auto_give_role ()

    if request.method =='POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view-profile', pk=pk)
    else:
        form = EditProfileForm(instance=profile)

    return render(request, 'profile/edit_profile.html', {'form': form, 'profile': profile})
