from django.urls import path
from .views import *

urlpatterns = [
    path('profile/<int:pk>', view_profile, name='view-profile'),
    path('edit_profile/<int:pk>', edit_profile, name='edit-profile')
]