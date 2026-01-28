from django.urls import path

from .import views

urlpatterns = [
    path('', views.home,name='home'),
    path('register/', views.register,name='register'),
    path('login/', views.login_view,name='login'),
    path('create_post/', views.create_post,name='create_post'),
    path('view_post/', views.view_post,name='view_post'),
    path('logout_view/', views.logout_view,name='logout_view'),
    path('post_detail/<int:post_id>', views.post_detail,name='post_detail'),
    path('edit_post/<int:post_id>', views.edit_post,name='edit_post'),
    path('delete_post/<int:post_id>', views.delete_post,name='delete_post'),
]