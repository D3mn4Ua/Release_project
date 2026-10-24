from django.urls import path
from .views import *

urlpatterns = [
    path('create_product/', create_product, name='create-product'),
    path('edit_product/<int:pk>', edit_product, name='edit-product'),
    path('delete_product/<int:pk>', delete_product, name='delete-product'),
    path('product_list', product_list, name='product-list'),
    path('product_detail/<int:pk>', product_detail, name='product-detail'),
    path('upload_image/', upload_image, name='upload-image'),
    path('gallery/', gallery, name='gallery'),
    path('image_detail/<int:pk>', image_detail, name='image-detail'),
    path("get_category_filters/", get_category_filters, name="get_category_filters"),
]