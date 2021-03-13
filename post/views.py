from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	liked = False

	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True

	# post.likes.add(request.user)
	return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))



def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats)
	context = {'cats': cats.title(), 'category_posts': category_posts }
	return render(request, 'post/categories.html', context)

def CategoryListView(request):
	cat_menu_list = Category.objects.all()
	context = {'cat_menu_list': cat_menu_list}
	return render(request, 'post/category_list.html', context)

class HomeView(ListView):
	model = Post
	template_name = 'post/home.html'
	ordering = ['-post_date']
	# ordering = ['-id']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context


class PostView(DetailView):
	model = Post
	template_name = 'post/post_detail.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(PostView, self).get_context_data(*args, **kwargs)

		stuff = get_object_or_404(Post, id=self.kwargs['pk'])
		total_likes = stuff.total_likes()

		liked = False

		if stuff.likes.filter(id=self.request.user.id).exists():
			liked = True

		context["cat_menu"] = cat_menu
		context["total_likes"] = total_likes
		context["liked"] = liked
		return context

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
