from django.contrib import admin
from .models import Category,Blogs

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','created_at','updated_at']
    search_fields = ['name']

class blogsadmin(admin.ModelAdmin):
    list_display = ['id','title','is_featured','status','category']
    search_fields = ['title','id','status','category__name']
    prepopulated_fields = {'slug':('title',)}
    list_editable = ['is_featured']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Blogs,blogsadmin)
