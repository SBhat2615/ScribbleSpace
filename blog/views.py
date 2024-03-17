from django.shortcuts import render
from django.http import HttpResponse

posts = [
  {
    "title" : "Blog Post 1",
    "author" : "Siddu",
    "date_posted" : "18 March",
    "content" : "First post content"
  },
  {
    "title" : "Blog Post 2",
    "author" : "Basu",
    "date_posted" : "18 April",
    "content" : "Second post content"
  }
]

# Create your views here.
def home(request):
  context = {
    "posts" : posts
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, "blog/about.html")