
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article, ArticleCategory, Comment
from user_management.models import Profile
from .forms import ArticleForm, CommentForm



def index(request):
    return HttpResponse('This is the wiki section of the hobby site midterm project for CSCI 40.')

def article_list(request):
    categories = ArticleCategory.objects.all()
    if request.user.is_authenticated:
        ctx = {
            "user_made": Article.objects.filter(author=Profile.objects.get(user=request.user)),
            "categories": categories
        }
    else:
        ctx = {
            "user_made": [],
            "categories": categories
        }
    
    return render(request, "wiki/article_list.html", ctx)
class ArticleListView(ListView):
    model = Article
    template_name = 'wiki/article_list.html'
    

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'wiki/article_detail.html'
    
    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        ctx = super().get_context_data(**kwargs)
        article = self.object
        ctx['article'] = article
        ctx["commentform"] = CommentForm()
        
        similar_readings = Article.objects.filter(category=article.category).exclude(pk=article.pk)
        ctx['similar_readings'] = similar_readings
        
        return ctx
    
    def post(self, request, *args, **kwargs):
        author = Profile.objects.get(user=request.user)
        article = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            comment.author = author
            comment.article = article
            comment.entry = form.cleaned_data.get('entry')
            comment.save()
            return self.get(request, *args, **kwargs)
        ctx = self.get_context_data(**kwargs) 
        return self.render_to_response(ctx)
    
        
        