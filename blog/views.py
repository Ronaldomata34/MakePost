from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, \
                                 UpdateView, DeleteView

from .models import Post
from .forms import PostForm


class PostList(ListView):
    model = Post
    context_object_name = 'posts'


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post

# but i want to do it with class bassed view, but i don't know how to do it
class NewPost(LoginRequiredMixin, CreateView): 
    model = Post
    template_name = 'blog/form.html'
    success_url = '/'
    fields = {'title','text','image'}

    def form_valid(self, form):
        #include user like author 
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/update.html'
    form_class = PostForm
    success_url = '/'


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name  = 'post_list.html'
    success_url = '/'






    

    
    
     
    
    









