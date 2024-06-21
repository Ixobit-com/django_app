from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from blog.forms import PostForm
from blog.models import Post


class BlogView(ListView):
    model = Post
    template_name = "blog/blog.html"


class AddPostView(CreateView):
    form_class = PostForm
    success_url = reverse_lazy("blog_all")
    template_name = "blog/create_post_form.html"
    model = Post


class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog_all")
    template_name = None




