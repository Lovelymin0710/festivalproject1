from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Comment
from .forms import CommentForm
from .forms import CreateBlog

# Create your views here.

def home(request):
    comments = Comment.objects.all()
    return render(request, 'index.html', {'comments':comments})

def comment_write(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
        comments = Comment.objects.all()
    return render(request, 'index.html', {'form':form, 'comments':comments})


def Lost(request):
    return render(request,'Lost.html')

def createBlog(request):

    if request.method == 'POST':
        form = CreateBlog(request.POST)
 
        if form.is_valid():
            form.save()
            return redirect('Lost')
        else:
            return redirect('index')
    else:
        form = CreateBlog()
        return render(request, 'createBlog.html', {'form': form})

    #form = CreateBlog()
 
    #return render(request, 'createBlog.html', {'form': form})