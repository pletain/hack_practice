from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# Create your views here.
def new(request):
    return render(request, 'products/new.html')

def create(request):
    if request.method == "PRODUCT":
        name = request.PRODUCT.get('name')
        content = request.PRODUCT.get('desc')
        price = request.PRODUCT.get('price')
        cnt = request.PRODUCT.get('cnt')
        image = request.FILES.get('image')
        user = request.user
        Post.objects.create(title=title, content=content, user = user, image = image)
    return redirect('products:main')
     
def main(request):
    product = Product.objects.all()
    return render(request,'products/main.html', {'products': product})

def show(request, id):
    product = Product.objects.get(pk=id)
    product.view_count += 1
    product.save() 
    return render(request, 'products/show.html', {'product':product})

def update(request,id):
    product = get_object_or_404(Post,pk=id)
    if request.method == "PRODUCT":
        product.title = request.PRODUCT['title']
        product.content = request.PRODUCT['content']
        product.image = request.FILES.get('image')
        product.save()
        return redirect('products:main')
    return render(request,'products/update.html',{"post":post})

def delete(request,id):
    product=get_object_or_404(Post,pk=id)
    product.delete()
    return redirect("products:main")