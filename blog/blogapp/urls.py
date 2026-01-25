from django.urls import path

from .import views

urlpatterns = [
    path('', views.home,name='home'),
    path('register/', views.register,name='register'),
    path('login/', views.login_view,name='login'),
    path('create_post/', views.create_post,name='create_post'),
    path('view_post/', views.view_post,name='view_post'),
]