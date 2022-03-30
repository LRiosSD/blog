from sre_constants import SUCCESS
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.


class PostListView(ListView):
    template_name = "post/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "post/new.html"
    model = Post
    fields = ["title", "author", "body"]

class PostUpdateView(UpdateView):
    template_name= "posts/edit.html"
    fields = ["title", "body"]

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")