from django.urls import  path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('category/<int:id>',views.category, name='category'),
    path('blog/<slug:slug>',views.blog,name='blog'),
    path('blogs/search/',views.search,name='search'),
    path('register/',views.register,name='register'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutpage,name='logout'),    


]