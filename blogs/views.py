from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from blogs.forms import UserForm
from .models import Blogs,Category,Comment
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request):
    # category = Category.objects.all()
    featured_post = Blogs.objects.filter(is_featured = True,status = 1)
    unfeatured_post = Blogs.objects.filter(is_featured = False)
    context = {
        # 'category':category,
        'featured_post':featured_post,
        'unfeatured_post':unfeatured_post,
    }
    return render(request,'index.html',context)



def category(request,id):
    # category = Category.objects.all()
    posts = Blogs.objects.filter(status=1,category=id)
    current_category = get_object_or_404(Category,id=id)
    context={
        'posts':posts,
        'current_category':current_category
    }
    return render(request,'blogs/category.html',context)


def blog(request,slug):
    posts = get_object_or_404(Blogs,slug=slug,status=1)
    # comments 
    comments = Comment.objects.filter(post=posts)
    comments_count = comments.count()

    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        post = posts

        Comment.objects.create(
                user = user,
                comment = comment,
                post = post,
                )
        
        return HttpResponseRedirect(request.path_info)

    
    context ={
        'post':posts,
        'comments':comments,
        'comments_count':comments_count
    }
    return render(request,'blogs/blog.html',context)

def search(request):
    key = request.GET.get('keyword','')
    post = Blogs.objects.filter(Q(title__icontains=key,status=1)| Q(short_body__icontains=key))
    context = {
        'posts':post,
        'key':key,
    }
    return render(request,'blogs/search.html',context)

def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('home')

    context ={
        'form':form
    }

    return render(request,'blogs/register.html',context)

def loginpage(request):
    form = AuthenticationForm()
   
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
    context = {
        'form':form,
    }
    return render(request,'blogs/login.html',context)

def logoutpage(request):
    logout(request)
    return redirect('home')

