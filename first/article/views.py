from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def article_list(request):
    articles=Article.objects.all().order_by('date')
    return render(request,'article/article_list.html',{'articles':articles})

def article_detail(request,name):
    article_d=Article.objects.get(slug=name)
    return render(request,'article/article_detail.html',{'article':article_d})

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method=='POST':
        form=forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('article:article_list')
    form=forms.CreateArticle()
    return render(request,'article/article_create.html',{'form':form})
