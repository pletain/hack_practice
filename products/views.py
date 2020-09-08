from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def new(request):
    return render(request, 'products/new.html')

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        cnt = request.POST.get('cnt')
        image = request.FILES.get('image')
        user = request.user
        Product.objects.create(name=name, desc=desc, price=price, user=user, cnt=cnt, image = image)
    return redirect('products:main')
     
def main(request):
    product = Product.objects.all().order_by('-created_at')
    return render(request,'products/main.html', {'product': product})

def show(request, id):
    product = Product.objects.get(pk=id)
    product.view_count += 1
    product.save() 
    all_comments = product.comments.all().order_by('-created_at')
    return render(request, 'products/show.html', {'product': product, 'comments': all_comments})

def update(request,id):
    product = get_object_or_404(Product,pk=id)
    if request.method == "POST":
        product.name = request.POST['name']
        product.desc = request.POST['desc']
        product.price = request.POST['price']
        product.cnt= request.POST['cnt']
        product.image = request.FILES.get('image')
        product.save()
        return redirect('products:main')
    return render(request,'products/update.html',{"product":product})

def delete(request,id):
    product=get_object_or_404(Product,pk=id)
    product.delete()
    return redirect("products:main")


def create_comment(request, post_id):    
    if request.method == "POST":
        product = get_object_or_404(Product, pk=post_id)
        current_user = request.user
        score = request.POST.get('score')
        comment_content = request.POST.get('content')
        Comment.objects.create(content=comment_content, writer=current_user, score=score, product = product)              
    return redirect('products:show', product.pk)

@login_required
def post_like(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.user in product.like_user_set.all():
        product.like_user_set.remove(request.user)
    else:
        product.like_user_set.add(request.user)
    
    if request.GET.get('redirect_to') == 'show':
        return redirect('products:show', product.pk)
    else:
        return redirect('products:main')

@login_required
def like_list(request):
    likes = request.user.like_set.all()
    return render(request,'products/like_list.html', {'likes': likes})