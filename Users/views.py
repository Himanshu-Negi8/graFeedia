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


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # username = request.POST['username']
            # email = request.POST['email']
            # first_name = request.POST['email']
            # last_name = request.POST['email']
            # course = request.POST['email']
            # email = request.POST['email']
            #
            # print(username)
            # # 'first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'course'
            # user_obj = User(username=form.cleaned_data['username'], email=form.cleaned_data['email'],
            #                 first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],
            #                 password1=form.cleaned_data['password1'],password2=form.cleaned_data['password2'],
            #                 course=form.cleaned_data['course'])
            # print(form.cleaned_data['course'])
            # user_obj.save()
            form.save()
            return redirect('Users:login')

    return render(request,'Users/signup.html',context={'key': form})


def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
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