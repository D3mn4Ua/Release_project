from django.urls import path
from .views import *

urlpatterns = [
    path('create_announcement/', create_announcement, name='create-announcement'),
    path('edit_announcement/<int:pk>/', edit_announcement, name='edit-announcement'),
    path('delete_announcement/<int:pk>/', delete_announcement, name='delete-announcement'),
    path('announcement_detail/<int:pk>/', announcement_detail, name='announcement-detail'),
    path('announcement_list/', announcement_list, name='announcement-list'),
]