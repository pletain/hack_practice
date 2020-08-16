from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

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
    product = Product.objects.all()
    return render(request,'products/main.html', {'product': product})

def show(request, id):
    product = Product.objects.get(pk=id)
    product.view_count += 1
    product.save() 
    return render(request, 'products/show.html', {'product':product})

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
    product=get_object_or_404(Post,pk=id)
    product.delete()
    return redirect("products:main")