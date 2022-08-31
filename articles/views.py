from pdb import post_mortem
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article, Post

# Create your views here.
class HomePageView(ListView):
    model = Article
    template_name = "home.html"
    
class BlogDetailView(DetailView):
    model = Article
    template_name = "post_list.html" 
