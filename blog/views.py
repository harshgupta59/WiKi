from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import random

class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name="blog/home.html"#<app>/<model>_<view_type>.html
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by = 5

class RandomPostListView(LoginRequiredMixin, ListView):
    model = Post.objects.order_by('?')
    template_name="blog/random.html"#<app>/<model>_<view_type>.html
    context_object_name='posts'

    def get_queryset(self):
        return random.sample(list(Post.objects.all()),1)
        

class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name="blog/user_posts.html"#<app>/<model>_<view_type>.html
    context_object_name='posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

#LoginRequiredMixin is used so that unauthorized user cannot access this page
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']
    template_name="blog/post_create.html"

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']
    template_name="blog/post_update.html"
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #to check if user is the one who creates it or not
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    success_url = '/'

@login_required
def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})

@login_required
def announcements(request):
    return render(request, 'blog/announcements.html',{'title': 'About'})


def SearchView(request):
    queryset=Post.objects.all()
    query=request.GET.get('q')
    if query:
        queryset=queryset.filter(title__icontains=query)
    return render(request,'blog/search.html',{
        "posts":queryset
    })






'''
class SearchView(ListView):
    model=Post
    template_name = 'blog/search.html'
    context_object_name='posts'
    paginate_by = 5

    def get_queryset(self):
        query = self.kwargs.get('q', '')
        object_list = self.model.objects.all()
        return Post.objects.filter(title__icontains=query).order_by('-date_posted')
'''