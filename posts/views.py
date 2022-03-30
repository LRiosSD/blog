from django.views.generic import (ListView, 
    DetailView)
from django.views.generic.edit import (CreateView,
     UpdateView, DeleteView)
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin)

# Create your views here.


class PostListView(ListView):
    template_name = "post/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "post/new.html"
    model = Post
    fields = ["title", "theme", "author", "body"]

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name= "posts/edit.html"
    fields = ["title", "theme", "body"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user