from blogs.models import Category,Blogs
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class categoryform(ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class postform(ModelForm):
    class Meta:
        model = Blogs
        fields = ['title','category','photo','short_body','body','status','is_featured']


class Userform(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','is_staff','groups']

class Editform(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','is_staff','groups']

