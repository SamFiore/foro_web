from django.shortcuts import render,redirect,get_object_or_404
from .models import PostModel,CommentModel
from .forms import PostForm,CommentForm
from django.contrib.auth import get_user
from django.contrib.auth.models import User
from datetime import datetime

# Create your views here.
def index(req):
    all_posts = PostModel.objects.order_by()
    return render(req,'index.html',{'all_posts':all_posts})

def create_post(req):
    if req.method == 'POST':
        author = get_user(req)
        post_model = PostModel.objects.create(name_post=req.POST['name_post'],txt_post=req.POST['txt_post'],author=author,date=datetime.now(tz=None))
        post_model.save()
        return redirect('index')
    post_form = PostForm()
    return render(req,'posts/create_post.html',{'post_form':post_form})

def details_post(req,id):
    post = get_object_or_404(PostModel,pk=id)
    if req.method == 'POST':
        author = get_user(req)
        comment_model = CommentModel.objects.create(comment=req.POST['comment'],post_nexus=post,author=author)
        comment_model.save()
        return redirect(f'/post_details/{id}')
    all_commentaries = CommentModel.objects.filter(post_nexus=post)
    comment_form = CommentForm()
    return render(req,'posts/details_post.html',{'post':post,'comment_form':comment_form,'all_commentaries':all_commentaries})

def self_profile(req):
    userModel = get_user(req)
    user_posts = PostModel.objects.filter(author=userModel)
    return render(req,'profile/self_profile.html',{'user_posts':user_posts})

def another_profile(req,id):
    user = get_object_or_404(User,pk=id)
    posts = PostModel.objects.filter(author=user)
    return render(req,'profile/other_profiles.html',{'another_user':user,'another_post':posts})


