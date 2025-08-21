from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Category,Blogs
from django.contrib.auth.decorators import login_required
from . forms import categoryform

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


