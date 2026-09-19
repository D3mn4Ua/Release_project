from django.shortcuts import render, redirect, get_object_or_404
from .forms import AnnouncementCreationForm
from django.contrib.auth.decorators import login_required
from .models import BlogAnnouncement

@login_required
def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementCreationForm(request.POST, request.FILES)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.creator = request.user.profile
            announcement.save()
            return redirect('announcement-list')
    else:
        form = AnnouncementCreationForm()

    return render(request, 'blog/announcement_create.html', {'form': form})

@login_required
def announcement_delete(request, pk):
    announcement = get_object_or_404(BlogAnnouncement, pk=pk)
    if request.method == 'POST':
        announcement.delete()
        return redirect('announcement-list')
    return render(request, 'blog/announcement_delete.html', {'announcement': announcement})

def announcement_list(request):
    announcements = BlogAnnouncement.objects.all()
    return render(request, 'blog/announcement_list.html', {'announcements': announcements})

def announcement_detail(request, pk):
    announcement = get_object_or_404(BlogAnnouncement, pk=pk)
    return render(request, 'blog/announcement_detail.html', {'announcement': announcement})