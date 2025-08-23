from django.urls import  path
from . import views

urlpatterns = [
    path('',views.dashboard, name = 'dashboard'),
    path('categories/',views.categories , name ='categories'),
    path('categories/add',views.add_category , name ='add_category'),
    path('categories/edit/<int:id>/',views.edit_category , name ='edit_category'),
    path('categories/delete/<int:id>/',views.delete_category , name ='delete_category'),
    path('posts/',views.posts, name = 'posts'),
    path('posts/add',views.post_add, name = 'post_add'),
    path('post/delete/<int:id>/',views.post_delete, name = 'post_delete'),
    path('post/edit/<int:id>/',views.post_edit, name = 'post_edit'),
    path('users/',views.users, name = 'users'),
    path('users/add',views.user_add, name = 'user_add'),
    path('users/edit/<int:id>/',views.user_edit, name = 'user_edit'),
    path('users/delete/<int:id>/',views.user_delete, name = 'user_delete'),
]