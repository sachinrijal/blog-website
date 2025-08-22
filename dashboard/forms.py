from blogs.models import Category,Blogs
from django.forms import ModelForm

class categoryform(ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class postform(ModelForm):
    class Meta:
        model = Blogs
        fields = ['title','category','photo','short_body','body','status','is_featured']

