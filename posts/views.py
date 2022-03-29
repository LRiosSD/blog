from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.


class PostListView(ListView):
    template_name = "post/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post