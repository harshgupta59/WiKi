from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    context= {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name="blog/home.html"#<app>/<model>_<view_type>.html
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by = 2

class PostDetailView(DetailView):
    model = Post

#LoginRequiredMixin is used so that unauthorized user cannot access this page
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']
    template_name="blog/post_create.html"

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    #success_url = 'post-detail'

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

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})