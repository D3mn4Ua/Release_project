from django.shortcuts import render, redirect, get_object_or_404
from .forms import AnnouncementCreationForm
from django.contrib.auth.decorators import login_required
from .models import BlogAnnouncement
from profiler.mixins import user_can_edit

@login_required
def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementCreationForm(request.POST, request.FILES)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.creator = request.user.profile
            announcement.save()
            return redirect('announcement-detail', pk=announcement.id)
    else:
        form = AnnouncementCreationForm()

    return render(request, 'blog/create_announcement.html', {'form': form})

@user_can_edit
def edit_announcement(request, pk):
    announcement = get_object_or_404(BlogAnnouncement, pk=pk)
    if request.method == 'POST':
        form = AnnouncementCreationForm(request.POST, request.FILES, instance=announcement)
        if form.is_valid():
            form.save()
            return redirect('announcement-detail', pk=pk)
    else:
        form = AnnouncementCreationForm(instance=announcement)
    return render(request, 'blog/edit_announcement.html', {'form': form})

@user_can_edit
def delete_announcement(request, pk):
    announcement = get_object_or_404(BlogAnnouncement, pk=pk)
    if request.method == 'POST':
        announcement.delete()
        return redirect('announcement-list')
    return render(request, 'blog/delete_announcement.html', {'announcement': announcement})

def announcement_list(request):
    announcements = BlogAnnouncement.objects.all()
    return render(request, 'blog/announcement_list.html', {'announcements': announcements})

def announcement_detail(request, pk):
    announcement = get_object_or_404(BlogAnnouncement, pk=pk)
    return render(request, 'blog/announcement_detail.html', {'announcement': announcement})