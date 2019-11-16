from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from Tutorial.models import TutorialCategory, TutorialSeries, Tutorial
from .forms import TutorialForm


class CreateTutorial(LoginRequiredMixin, CreateView):
    model = Tutorial
    form_class = TutorialForm


    def form_valid(self, form):
        self.object = form.save(commit=False)
        user = self.request.user

        self.object.user = user
        self.object.save()
        return super(CreateTutorial,self).form_valid(form)




def tutorial_category(request):
    cat = TutorialCategory.objects.all()
    context = {'category': cat}
    return render(request, 'Tutorial/category.html', context)


def tutorial_series(request, slug):
    category = slug
    se = TutorialSeries.objects.filter(tutorial_category__category_slug=category)
    context = {'series': se}
    return render(request, 'Tutorial/series.html', context)

# for c in TutorialCategory.objects.all():
#     categories = c.category_slug
#     if single_slug in categories:
#         TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
