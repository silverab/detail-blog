from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, EditForm

class HomeView(ListView):
	model = Post
	template_name = 'post/home.html'

class PostView(DetailView):
	model = Post
	template_name = 'post/post_detail.html'

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'post/add_post.html'
	# fields = '__all__'
	# fields = ('title', 'body')

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'post/update_post.html'
	# fields = ['title', 'title_tag', 'body']