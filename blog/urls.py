from django.urls import path
from .views import *

urlpatterns = [
    path('announcement/create/', create_announcement, name='create-announcement'),
    path('announcement/edit/<int:pk>/', edit_announcement, name='edit-announcement'),
    path('announcement/delete/<int:pk>/', delete_announcement, name='delete-announcement'),
    path('announcement/detail/<int:pk>/', announcement_detail, name='announcement-detail'),
    path('announcement/list/', announcement_list, name='announcement-list'),
]