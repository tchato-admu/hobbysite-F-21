
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

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
    
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'wiki/article_create.html'
    
    def get_success_url(self):
        return reverse_lazy('wiki:article_detail', kwargs={ 'pk': self.object.pk })
    
    def form_valid(self, form):
        author = Profile.objects.get(user=self.request.user)
        form.instance.author = author
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        author = Profile.objects.get(user=self.request.user)
        ctx['createform'] = ArticleForm(initial={'author': author})
        return ctx
    
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'wiki/article_update.html'
    
    def get_success_url(self):
        return reverse_lazy('wiki:article_detail', kwargs={ 'pk': self.object.pk })
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['article'] = Article.objects.get(pk=self.object.pk)
        return ctx
    
              
        