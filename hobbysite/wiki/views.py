from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Article

def index(request):
    return HttpResponse('This is the wiki section of the hobby site midterm project for CSCI 40.')

class ArticleListView(ListView):
    model = Article
    template_name = 'wiki/article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'wiki/article_detail.html'