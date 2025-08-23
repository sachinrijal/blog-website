from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Category,Blogs
from django.contrib.auth.decorators import login_required
from . forms import categoryform,postform,Userform,Editform
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url="login")
def dashboard(request):
    category_count = Category.objects.all().count()
    blog_count = Category.objects.all().count()
    context = {
        'category_count':category_count,
        'blog_count':blog_count,
        }


    return render(request,'dashboard/dashboard.html',context)

def categories(request):
    return render(request,'dashboard/categories.html',context={})

def add_category(request):
    form = categoryform()
    if request.method == "POST":
        form = categoryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    context = {
        'form':form,
    }

    return render(request,'dashboard/add_category.html',context)

def edit_category(request,id):
    category_edit = get_object_or_404(Category,id=id)
    form = categoryform(instance=category_edit)
    
    if request.method == 'POST':
        form = categoryform(request.POST,instance=category_edit)
        if form.is_valid():
            form.save()
            return redirect('categories')

    context ={
        'form':form,
        'category_edit':category_edit,
    }
    return render(request,'dashboard/edit_category.html',context)

def delete_category(request,id):
    category = get_object_or_404(Category,id=id)
    # print(category)
    if request.method == "POST":
        action = request.POST.get('action')
        if action == 'Yes':
            category.delete()
            return redirect('categories')
            
        else:
            return redirect('categories')
    return render(request,'dashboard/delete_category.html')

def posts(request):
    posts = Blogs.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'dashboard/posts.html',context)

def post_add(request):
    form = postform()
    if request.method == 'POST':
        form = postform(request.POST, request.FILES) 
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('posts')
        
    context = {
        'form':form,
    }
    return render(request,'dashboard/post_add.html',context)

def post_delete(request,id):
    post = get_object_or_404(Blogs,id=id)
    post.delete()
    return redirect('posts')

def post_edit(request,id):
    post = get_object_or_404(Blogs,id=id)
    form = postform(instance=post)

    if request.method == "POST":
        form = postform(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = post.author
            post.save()

            return redirect('posts')

    context ={
        'form':form
    }
    return render(request,'dashboard/post_edit.html', context)

def users(request):
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request,'dashboard/user.html',context)


def user_add(request):
    form = Userform()
    if request.method == "POST":
        form = Userform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        
    context = {
        'form':form,
    }
    return render(request,'dashboard/user_add.html',context)

def user_edit(request,id):
    user = get_object_or_404(User,id=id)
    form = Editform(instance=user)
    if request.method == "POST":
        form = Editform(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    context = {
        'form':form
    }
    return render(request,'dashboard/user_edit.html',context)

def user_delete(request,id):
    user = get_object_or_404(User,id=id)
    user.delete()
    return redirect('users')




