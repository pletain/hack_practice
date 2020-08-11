from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# Create your views here.
def new(request):
    return render(request, 'product/new.html')

def create(request):
    if request.method == "PRODUCT":
        name = request.PRODUCT.get('name')
        content = request.PRODUCT.get('desc')
        price = request.PRODUCT.get('price')
        cnt = request.PRODUCT.get('cnt')
        image = request.FILES.get('image')
        user = request.user
        Post.objects.create(title=title, content=content, user = user, image = image)
    return redirect('product:main')
     
def main(request):
    product = Product.objects.all()
    return render(request,'product/main.html', {'product': product})

def show(request, id):
    post = Post.objects.get(pk=id)
    A = post.view_count
    A = A + 1
    post.view_count = A
    post.save() 
    return render(request, 'product/show.html', {'product':product})

def update(request,id):
    post = get_object_or_404(Post,pk=id)
    if request.method == "PRODUCT":
        post.title = request.PRODUCT['title']
        post.content = request.PRODUCT['content']
        post.image = request.FILES.get('image')
        post.save()
        return redirect('product:main')
    return render(request,'product/update.html',{"post":post})

def delete(request,id):
    product=get_object_or_404(Post,pk=id)
    product.delete()
    return redirect("product:main")