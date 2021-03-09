from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats)
	context = {'cats': cats.title(), 'category_posts': category_posts }
	return render(request, 'post/categories.html', context)

class HomeView(ListView):
	model = Post
	template_name = 'post/home.html'
	ordering = ['-post_date']
	ordering = ['-id']

class PostView(DetailView):
	model = Post
	template_name = 'post/post_detail.html'

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'post/add_post.html'
	# fields = '__all__'
	# fields = ('title', 'body')

class AddCategoryView(CreateView):
	model = Category
	template_name = 'post/add_category.html'
	fields = '__all__'
	# form_class = PostForm
	# fields = ('title', 'body')

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'post/update_post.html'
	# fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
	model = Post
	template_name = 'post/delete_post.html'
	success_url = reverse_lazy('home')
