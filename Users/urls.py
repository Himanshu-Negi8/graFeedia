from django.urls import path,include
from Users import views

app_name = 'Users'


urlpatterns = [
        path('signup/',views.SignupView.as_view(),name='signup'),
        path('login/',views.loginview,name='login'),
        path('logout/', views.logOut, name='logout'),
        path('profile/<slug:slug>', views.ProfileView.as_view(), name='user_profile')
]
