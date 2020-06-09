from django.urls import path
from . import views
app_name='Tutorial'

urlpatterns = [
    path('<slug:slug>/add_tutorial/',views.CreateTutorial.as_view(),name='addtutorial'),
    path('category/',views.tutorial_category,name='tut_category'),
    path('<slug:slug>/series/',views.tutorial_series,name='tut_series'),
    path('tutorial_detail/<slug:slug>',views.TutorialDetailView.as_view(),name='tutorial_detail'),
]
