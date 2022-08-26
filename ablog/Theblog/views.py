from django.db.models import fields
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,RedirectView
from .models import Post
from .forms import PostForm,EditForm
from django.urls import reverse_lazy
# Create your views here.
#def home(request):
    #return render(request,'home.html',{})



class HomeView(ListView):
    model=Post
    template_name='home.html'
    ordering= ['-post_date']
    #ordering= ['-id'] # '-'  here represents ascending order 

class ArticleDetailView(DetailView):
    model= Post
    template_name='article_details.html'

class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name='add_post.html'
    #fields= '__all__'
    #fields=('title', 'body')
    success_url= reverse_lazy('home')

class UpdatePostView(UpdateView):
    model=Post
    form_class= EditForm
    template_name= 'update_post.html'
    #fields= ['title', 'title_tag','body']

class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url= reverse_lazy('home')

class RedirectView(DeleteView):
    model=Post
    template_name='redirect.html'
    success_url= reverse_lazy('redirect')

    