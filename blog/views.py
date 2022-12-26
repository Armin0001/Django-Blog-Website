from django.shortcuts import render, get_object_or_404
from django .contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)
from .models import Post


def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html' #this still lists all of the posts from a post model, but we want to add a filter
	context_object_name = 'posts' #to this that only gets the post from a certain user, that is going to come directly
	#ordering = ['-date_posted'] #from the URL. When we create a new url pattern for this, we will specify a username and
	paginate_by = 5 #url path itself. 
	
	def get_queryset(self): #now we want to get the user, associated with the username that we are going to get from the url
		user = get_object_or_404(User, username = self.kwargs.get('username'))	#if the user doesn't exit, we are going
		return Post.objects.filter(author=user).order_by('-date_posted')	#to return 404 telling the page doesn't exist
													# if the user exist, we are going to capture them in the user variable
	# return Post.objects.order_by('-date_posted').filter(author=user) use for django version > 3
	# return Post.objects.filter(author=user).order_by('-date_posted') currently using and it works
class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/' #deletion now knows where to redirect

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request, 'blog/about.html', {'title':'About'})



