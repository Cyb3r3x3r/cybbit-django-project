from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('posts')
            except IntegrityError:
                return render(request, 'signup.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'signup.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'index.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'index.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('posts')

@login_required
def posts(request):
    posts = Post.objects.all().order_by('-created')
    context = {
        "posts": posts,
    }
    return render(request,'posts.html',context)
    
@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
        
@login_required
def createpost(request):
    if request.method == 'GET':
        return render(request, 'posts.html', {'form':PostForm()})
    else:
        try:
            form = PostForm(request.POST)
            newPost = form.save(commit=False)
            newPost.user = request.user
            newPost.save()
            return redirect('posts')
        except ValueError:
            return render(request, 'posts.html', {'form':PostForm(), 'error':'Bad data passed in. Try again.'})

@login_required
def viewpost(request,pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post":post
    }
    return render(request,'viewpost.html',context)