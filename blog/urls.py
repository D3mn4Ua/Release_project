from django.urls import path
from .views import *

urlpatterns = [
    path('announcement_create/', create_announcement, name='create-announcement'),
    path('announcement_list/', announcement_list, name='announcement-list'),
    path('announcement_detail/<int:pk>/', announcement_detail, name='announcement-detail'),
    path('announcement_delete/<int:pk>/', announcement_delete, name='announcement-delete')
]