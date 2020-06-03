from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Post
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
class PostView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['text']
    template_name = 'create_post.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('home')
