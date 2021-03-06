from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

class HomeView(ListView):
	model = Post
	template_name = 'post/home.html'

class PostView(DetailView):
	model = Post
	template_name = 'post/post_detail.html'

class AddPostView(CreateView):
	model = Post
	template_name = 'post/add_post.html'
	fields = '__all__'
	# fields = ('title', 'body')