from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Profile, Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):

    if request.method == 'GET':
        post_list = Post.objects.all()
        return render(request, 'home/home.html' , {'post_list': post_list})


    return render(request, 'home/home.html')

def register(request):

    if request.method == 'POST':
        username = request.POST.get('first_name')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date_of_birth')


        if User.objects.filter(username=username).exists():
             return render(request, 'auth/register.html', {'error': 'Username allready exists'})
        user = User.objects.create_user(username=username,
                                        password=password,
                                        email=email,
                                        first_name=first_name,
                                        last_name=last_name)
        Profile.objects.create(
            username=user,
            phone=phone,
            address=address,
            date_of_birth=date_of_birth
        )

        return render(request, 'auth/register.html')
    else:
        return render(request, 'auth/register.html', {'message': 'User registered successfully'})


def login_view(request):

    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        try:
            profile = Profile.objects.get(phone=phone)
            user = authenticate(
                username=profile.username.username,
                password=password
            )
            
            if user:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'auth/login.html', {'error': 'Invalid credentials.'})

        except Profile.DoesNotExist:
            return render(request, 'auth/login.html', {'error': 'Phone number not found.'})

    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Post.objects.create(
            title=title,
            description=description,
            created_by=request.user,
        )

        return redirect('home')

    return render(request, 'posts/create_post.html')

@login_required
def view_post(request):

    if request.method == 'GET':
        post_list = Post.objects.filter(created_by=request.user)
        return render(request, 'posts/my_post.html' , {'post_list': post_list})

def post_detail(request, post_id):

    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/post_details.html', {'post': post})

@login_required
def edit_post(request, post_id):

    post = get_object_or_404(Post, id=post_id, created_by=request.user)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.description = request.POST.get('description')
        post.save()
        return redirect('view_post')

    return render(request, 'posts/post_edit.html', {'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, created_by=request.user)
    post.delete()
    return redirect('view_post')
    
