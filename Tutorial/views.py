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
        series = TutorialSeries.objects.get(series_slug=self.kwargs['slug'])
        print(series)
        self.object.user = user
        self.object.tutorial_series = series
        self.object.save()
        return super().form_valid(form)


def tutorial_category(request):
    cat = TutorialCategory.objects.all()
    context = {'category': cat}
    return render(request, 'Tutorial/category.html', context)


def tutorial_series(request, slug):
    category = slug
    se = TutorialSeries.objects.filter(tutorial_category__category_slug=category)
    context = {'series': se}
    return render(request, 'Tutorial/series.html', context)


class TutorialListView(ListView):
    model = Tutorial
    template_name = 'Tutorial/tutorial_list.html'
    # select_related = 'tutorial_series'

    def get_queryset(self):
        ob = TutorialSeries.objects.get(series_slug=self.kwargs['slug'])
        print(ob)
        return Tutorial.objects.filter(tutorial_series=ob)


class TutorialDetailView(DetailView):
    model = Tutorial

    def get_object(self, queryset=None):
        slug =self.kwargs['slug']
        ob = Tutorial.objects.get(tutorial_slug=slug)
        try :
            obj = Tutorial.objects.get(tutorial_title=ob)
        except Tutorial.DoesNotExist:
            obj = None;
        return obj
    # def get_queryset(self):
    #     print(self.kwargs['slug'])
    #     ob = Tutorial.objects.get(tutorial_slug=self.kwargs['slug'])
    #     print(ob)
    #     return Tutorial.objects.filter(tutorial_title=ob)

# for c in TutorialCategory.objects.all():
#     categories = c.category_slug
#     if single_slug in categories:
#         TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
