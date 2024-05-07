from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article, ArticleCategory
from user_management.models import Profile
from .forms import ArticleForm, CommentForm


class AuthorProfileMixin(object):
    def get_author_profile(self):
        if self.request.user.is_authenticated:
            author, _ = Profile.objects.get_or_create(user=self.request.user)
            return author
        return None

class ArticleListView(AuthorProfileMixin, ListView):
    model = ArticleCategory 
    template_name = 'blog/article_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.get_author_profile()
        if author:
            articles_by_author = Article.objects.filter(author=author)
            context['articles_by_author'] = articles_by_author
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.object  # Retrieve the article object from the view
        context['article'] = article

        #article from same author
        articles_by_author = Article.objects.filter(author=article.author).exclude(pk=article.pk)
        context['articles_by_author'] = articles_by_author

        if self.request.user.is_authenticated:
            author_profile = Profile.objects.filter(user=self.request.user).first()
            context['author_profile'] = author_profile
            context['comment_form'] = CommentForm()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        author = Profile.objects.get(user=self.request.user)
        article = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = author
            comment.article = article
            comment.save()
            return redirect('blog:article_detail', pk=article.pk)
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
    
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_create.html'

    def get_success_url(self):
        return reverse_lazy('blog:article_detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        author = Profile.objects.get(user=self.request.user)
        form.instance.author = author
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = Profile.objects.get(user=self.request.user)
        context['form'] = ArticleForm(initial={'author': author})
        return context

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_update.html'

    def get_success_url(self):
        return reverse_lazy('blog:article_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)