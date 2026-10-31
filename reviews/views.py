from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from products.models import Product
from .forms import AddReviewForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def add_review(request, pk):
    reviewed_product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = AddReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user.profile
            review.product = reviewed_product
            review.save()
            return redirect('product-detail', pk=reviewed_product.pk)
    else:
        form = AddReviewForm()

    return render(request, 'reviews/add_review.html', {'form': form, 'product': reviewed_product})

def product_review_list(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    reviews_list = Review.objects.filter(product=product)

    paginator = Paginator(reviews_list, 5)
    page_number = request.GET.get('page')
    reviews = paginator.get_page(page_number)
    
    return render(request, 'reviews/review_list.html', {'product': product, 'reviews': reviews, 'is_paginated': reviews.has_other_pages()})

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)

    return render(request, 'reviews/review_detail.html', {'review': review})

@login_required
def review_edit(request, pk):
    review = get_object_or_404(Review, pk=pk)
        
    if request.method == 'POST':
        form = AddReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('detail-review', pk=review.pk)
    else:
        form = AddReviewForm(instance=review)
        
    return render(request, 'reviews/edit_review.html', {'form': form, 'review': review})

@login_required
def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.method == 'POST':
        review.delete()
        return redirect('product-list')

    return render(request, 'reviews/delete_review.html', {'review': review,})