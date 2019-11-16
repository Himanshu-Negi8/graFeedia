from django.shortcuts import render
from braces.views import SelectRelatedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, DeleteView
# Create your views here.
from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        user = self.request.user
        self.object.user = user
        self.object.save()
        return super().form_valid(form)
