from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import SignupForm
from .models import User

class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'Users/signup.html'
    success_url = reverse_lazy('home')


def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Such a user does not exist')
            return redirect('Users:login')
    return render(request, 'Users/login.html')


@login_required
def logOut(request):
    logout(request)
    return redirect('home')


class ProfileView(LoginRequiredMixin, DetailView):
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        obj = User.objects.filter(user=self.request.user)
        context['user'] =obj
        return context