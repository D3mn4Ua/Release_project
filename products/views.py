from django.shortcuts import render, redirect, get_object_or_404
from .models import Product_test, Image, Product, Category
from .forms import ProductCreationForm, ImageCreationForm
from profiler.mixins import user_can_edit
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.exceptions import ValidationError
from django.http import JsonResponse

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductCreationForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user.profile
            product.save()
            return redirect('product-list')
        else:
            raise ValidationError('Given data was not validated')
    else:
        form = ProductCreationForm()

    return render(request, 'product/create_product.html', {'form': form})

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    else:
        form = ImageCreationForm()
    return render(request, 'gallery/upload_image.html', {'form': form})

@login_required
@user_can_edit
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductCreationForm(request.POST, instance=product)
        if form.is_valid:
            form.save()
            return redirect('product-detail', pk=pk)
    else:
        form = ProductCreationForm(instance=product)

    return render(request, 'product/edit_product.html', {'form': form})

@login_required
@user_can_edit
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product-list')
    return render(request, 'product/delete_product.html', {'product': product})

def product_list(request):
    filters = {}
    attribute_filters = {}

    category_id = request.GET.get("category")
    if category_id:
        filters["category_id"] = category_id
        category = Category.objects.get(id=category_id)
        available_attrs = category.attributes.keys()
    else:
        category = None
        available_attrs = []

    for key, value in request.GET.items():
        if not value or key == "category" or key == "page":
            continue
        if key in available_attrs:
            attribute_filters[f"additional_info__{key}"] = value

    products = Product.objects.filter(**filters).filter(**attribute_filters)

    paginator = Paginator(products, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "product/product_list.html", {
        "page_obj": page_obj,
        "products": page_obj.object_list,
        "categories": Category.objects.all(),
        "current_category": category,
    })


def get_category_filters(request):
    category_id = request.GET.get("category")
    if not category_id:
        return JsonResponse({}, safe=False)

    category = Category.objects.get(id=category_id)
    available_attrs = category.attributes.keys()

    filters = {}
    for key in available_attrs:
        values = (
            Product.objects.filter(category=category)
            .values_list(f"additional_info__{key}", flat=True)
            .distinct()
        )
        filters[key] = list(values)

    return JsonResponse(filters)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product_detail.html', {'product': product})

def gallery(request):
    images = Image.objects.all()    
    paginator = Paginator(images, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'gallery/gallery.html', {'page_obj': page_obj, 'images': images})

def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    products = Product.objects.filter(seller=request.user.profile)

    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product = get_object_or_404(Product, pk=product_id, seller=request.user.profile)
        image.products.add(product)
        messages.success(request, f'Фото добавлено к продукту {product.title}')
        return redirect('image-detail', pk=image.pk)

    return render(request, "gallery/image_detail.html", {"image": image, "products": products})
