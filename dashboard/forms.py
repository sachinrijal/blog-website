from blogs.models import Category
from django.forms import ModelForm

class categoryform(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
