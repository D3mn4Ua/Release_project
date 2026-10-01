from django.shortcuts import render, redirect, get_object_or_404
from .models import Product_test
from .forms import ProductCreationForm
from profiler.mixins import user_can_edit
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductCreationForm(request.POST)
        if form.is_valid:
            product = form.save(commit=False)
#            product.seller = request.user.profile
            product.save()
            return redirect('product-list')
    else:
        form = ProductCreationForm()

    return render(request, 'product/create_product.html', {'form': form})

@user_can_edit
def edit_product(request, pk):
    product = get_object_or_404(Product_test, pk=pk)
    if request.method == 'POST':
        form = ProductCreationForm(request.POST, instance=product)
        if form.is_valid:
            form.save()
            return redirect('product-detail', pk=pk)
    else:
        form = ProductCreationForm(instance=product)

    return render(request, 'product/edit_product.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Product_test, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product-list')
    return render(request, 'product/delete_product.html', {'product': product})

def product_list(request):
    products = Product_test.objects.all()
    paginator = Paginator(products, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'product/product_list.html', {'page_obj': page_obj, 'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product_test, pk=pk)
    return render(request, 'product/product_detail.html', {'product': product})