from django.shortcuts import render
from django.http import HttpResponse


posts = [
	{
		'author': 'John Snow',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'July 2, 2020'
	},
	{
		'author': 'Drew Harley',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'July 3, 2020'
	}
]



def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)
	

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
	