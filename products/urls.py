from django.urls import path
from .views import *

urlpatterns = [
    path('product/create/', create_product, name='create-product'),
    path('product/edit//<int:pk>/', edit_product, name='edit-product'),
    path('product/delete/<int:pk>/', delete_product, name='delete-product'),
    path('product/list/', product_list, name='product-list'),
    path('product/detail/<int:pk>/', product_detail, name='product-detail'),
    path('image/upload/', upload_image, name='upload-image'),
    path('gallery/', gallery, name='gallery'),
    path('image/detail/<int:pk>/', image_detail, name='image-detail'),
    path("get_category_filters/", get_category_filters, name="get_category_filters"),
    path('buy/', buy, name='buy')
]