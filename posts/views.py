from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, User
# Create your views here.
def new(request):
    return render(request, 'posts/new.html')

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        cnt = request.POST.get('cnt')
        image = request.FILES.get('image')
        current_user = request.user
        post = Post.objects.create(name=name, desc=desc, price=price, user=current_user, cnt=cnt, image = image)
    return redirect(request, 'posts/main.html')
     
def main(request):
    post = Post.objects.all().order_by('-created_at')
    return render(request,'posts/main.html', {'post': post})

def show(request, id):
    post = Post.objects.get(pk=id)
    post.view_count += 1
    post.save() 
    all_comments = post.comments.all().order_by('-created_at')
    return render(request, 'posts/show.html', {'post': post, 'comments': all_comments})

def update(request,id):
    post = get_object_or_404(Post,pk=id)
    if request.method == "POST":
        post.name = request.POST['name']
        post.desc = request.POST['desc']
        post.price = request.POST['price']
        post.cnt= request.POST['cnt']
        post.image = request.FILES.get('image')
        post.save()
        return redirect('posts:main')
    return render(request,'posts/update.html',{"post":post})

def delete(request,id):
    post=get_object_or_404(Post,pk=id)
    post.delete()
    return redirect("posts:main")


def create_comment(request, post_id):    
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        current_user = request.user
        score = request.POST.get('score')
        comment_content = request.POST.get('content')
        Comment.objects.create(content=comment_content, writer=current_user, score=score, post = post)              
    return redirect('posts:show', post.pk)

@login_required
def post_like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if request.user in post.like_user_set.all():
        post.like_user_set.remove(request.user)
    else:
        post.like_user_set.add(request.user)
    
    if request.GET.get('redirect_to') == 'show':
        return redirect('posts:show', post.pk)
    else:
        return redirect('posts:main')

@login_required
def like_list(request):
    likes = request.user.like_set.all()
    return render(request,'posts/like_list.html', {'likes': likes})