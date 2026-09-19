from django.urls import path
from .views import *

urlpatterns = [
    path('edit_profile/<int:pk>', edit_profile, name='edit-profile'),
    path('profile/<int:pk>', profile_detail, name='profile-detail'),
]