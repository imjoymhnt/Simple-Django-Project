from django.urls import path
from . import views


urlpatterns = [
    path('accounts/signup/', views.SignupView.as_view(), name='signup'),
    path('', views.PostView.as_view(), name='home'),
    path('create/', views.PostCreateView.as_view(), name = 'create')
]
