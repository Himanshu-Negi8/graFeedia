from django.contrib.auth import get_user_model
from django.shortcuts import render
from braces.views import SelectRelatedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.http import Http404, request
from django.views.generic import ListView, DetailView, CreateView, DeleteView
# Create your views here.
from .models import Post
from .forms import PostForm

User = get_user_model()


class PostListView( ListView):
    model = Post

    # def get_queryset(self):
    #     try:
    #         self.post_user = Post.objects.filter(user=self.request.user)
    #     except User.DoesNotExist:
    #         return render(request, 'home.html')
    #
    #
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['post_user'] = self.post_user
    #     return context


# def PostListView(request):
#     user = request.user
#     user_posts = Post.objects.filter(user=user).order_by('-created_at')
#     template = 'post_list.html'
#     context = {'posts':user_posts}
#     return render(request,template,context)

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        user = self.request.user
        self.object.user = user
        self.object.save()
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
