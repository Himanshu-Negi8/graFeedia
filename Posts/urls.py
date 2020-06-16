from django.urls import path
from . import views

app_name = 'Posts'

urlpatterns = [
    # path('createpost/', views.CreatePostView.as_view(), name='createPost'),
    path('createpost', views.createPost,name='createPost'),
    path('post_list/',views.PostListView.as_view(),name='post_lists'),

    path('post_detail/<slug:slug>',views.PostDetailView.as_view(),name='post_detail'),

]