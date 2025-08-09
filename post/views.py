from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView,DeleteView,UpdateView
from .models import Post
from django.urls import reverse_lazy

class PostListView(ListView):
    template_name="post/list.html"
    model=Post



class PostDetailView(DetailView):
    template_name= "post/detail.html"
    model=Post
    context_object_name="single_post"



class PostCreateView(CreateView):
    template_name = "post/new.html"
    model=Post
    context_object_name="new_post"
    fields =["title","subtitle","body"]


class PostUpdateView(UpdateView):
    template_name = "post/edit.html"
    model=Post
    fields= ["title","subtitle ","body"]



class PostDeleteView(DeleteView):
    template_name= "post/delete.html"
    model=Post
    success_url = reverse_lazy("post_list")
