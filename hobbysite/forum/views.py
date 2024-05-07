from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Thread, ThreadCategory
from user_management.models import Profile
from .forms import ThreadForm, CommentForm


class AuthorProfileMixin(object):
    def get_author_profile(self):
        if self.request.user.is_authenticated:
            author, _ = Profile.objects.get_or_create(user=self.request.user)
            return author
        return None

class ThreadListView(ListView):
    model = ThreadCategory
    template_name = 'forum/thread_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        author = AuthorProfileMixin.get_author_profile(self)
        if author:
            threads_by_author = Thread.objects.filter(author=author)
            context['threads_by_author'] = threads_by_author
        return context

class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'forum/thread_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        thread = self.object  
        context['thread'] = thread

        same_category_threads = Thread.objects.filter(category=thread.category).exclude(pk=thread.pk)
        context['same_category_threads'] = same_category_threads

        if self.request.user.is_authenticated:
            author_profile = Profile.objects.filter(user=self.request.user).first()
            context['author_profile'] = author_profile
            context['comment_form'] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        author = Profile.objects.get(user=self.request.user)
        thread = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = author
            comment.thread = thread
            comment.save()
            return redirect('forum:thread_detail', pk=thread.pk)
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
    
class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    form_class = ThreadForm
    template_name = 'forum/thread_create.html'

    def get_success_url(self):
        return reverse_lazy('forum:thread_detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        author = Profile.objects.get(user=self.request.user)
        form.instance.author = author
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = Profile.objects.get(user=self.request.user)
        context['form'] = ThreadForm(initial={'author': author})
        return context
    
class ThreadUpdateView(LoginRequiredMixin, UpdateView):
    model = Thread
    form_class = ThreadForm
    template_name = 'forum/thread_update.html'

    def get_success_url(self):
        return reverse_lazy('forum:thread_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)