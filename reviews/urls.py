from core.urls import path
from .views import *

urlpatterns = [
    path('review/add/product/<int:pk>/', add_review, name='add-review'),
    path('review/list/product/<int:product_pk>', product_review_list, name='list-reviews'),
    path('review/detail/<int:pk>', review_detail, name='detail-review'),
    path('review/edit/<int:pk>', review_edit, name='edit-review'),
    path('review/delete/<int:pk>', review_detail, name='delete-review')
]